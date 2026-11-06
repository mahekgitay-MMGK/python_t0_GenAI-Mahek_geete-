"""Interactive GenAI chat app using an OpenAI-compatible API.

Step-by-step explanation
1. Set OPENAI_API_KEY in your environment. Optionally set OPENAI_MODEL or
	OPENAI_BASE_URL to choose a compatible model or provider.
2. main() checks the key, creates conversation history with the system
	message, and prints the startup instructions.
3. Each non-empty message is added to history. get_reply() sends the full
	conversation to the provider's /chat/completions endpoint.
4. The response is added to history and displayed. If a request fails, its
	user message is removed and the error is printed to stderr.
5. Use /reset to clear the conversation, /exit or /quit to stop, or Ctrl+C
	or end-of-file to quit cleanly.

Output notes
- Startup shows the selected model and the /reset and /exit commands.
- Successful turns show a ``You:`` prompt and then ``AI: <reply>``.
- /reset prints ``Chat history cleared.``; quitting prints ``Goodbye!``.
- A missing key or request failure prints an error. Assistant text varies
  according to the selected model and provider.

Run with: ``python Day_10_projGenAI.py``
"""

import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
SYSTEM_MESSAGE = "You are a helpful assistant. Answer clearly and accurately."
REQUEST_TIMEOUT = 60
MAX_HISTORY_TURNS = 10


def show_help():
	"""Display available chat commands."""
	print("Commands: /help, /reset, /exit (or /quit)")


def get_reply(messages):
	"""Request a response from the chat completions endpoint."""
	data = json.dumps({"model": MODEL, "messages": messages}).encode("utf-8")
	request = Request(
		f"{BASE_URL}/chat/completions",
		data=data,
		headers={
			"Authorization": f"Bearer {API_KEY}",
			"Content-Type": "application/json",
		},
		method="POST",
	)
	try:
		with urlopen(request, timeout=REQUEST_TIMEOUT) as response:
			result = json.loads(response.read().decode("utf-8"))
		reply = result["choices"][0]["message"]["content"]
		if not isinstance(reply, str) or not reply.strip():
			raise RuntimeError("The AI service returned an empty or invalid reply.")
		return reply.strip()
	except HTTPError as exc:
		message = exc.read().decode("utf-8", errors="replace")
		raise RuntimeError(f"API returned HTTP {exc.code}: {message}") from exc
	except (URLError, TimeoutError) as exc:
		raise RuntimeError(f"Unable to connect to the AI service: {exc}") from exc
	except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
		raise RuntimeError("The AI service returned an invalid response.") from exc


def main():
	if not API_KEY:
		print(
			"Cannot start: OPENAI_API_KEY is not set.\n"
			"Set your API key in the terminal before running this script:\n"
			'  PowerShell: $env:OPENAI_API_KEY = "your-api-key"\n'
			"  Command Prompt: set OPENAI_API_KEY=your-api-key\n"
			"Then run the script again. Do not share or commit your API key."
		)
		return 1

	history = [{"role": "system", "content": SYSTEM_MESSAGE}]
	print(f"GenAI Chat ({MODEL}) | /help for commands")
	while True:
		try:
			text = input("\nYou: ").strip()
		except (EOFError, KeyboardInterrupt):
			print("\nGoodbye!")
			return 0

		if not text:
			continue
		command = text.casefold()
		if command in {"/exit", "/quit"}:
			print("Goodbye!")
			return 0
		if command == "/help":
			show_help()
			continue
		if command == "/reset":
			history = [{"role": "system", "content": SYSTEM_MESSAGE}]
			print("Chat history cleared.")
			continue

		history.append({"role": "user", "content": text})
		try:
			reply = get_reply(history)
		except RuntimeError as exc:
			history.pop()
			print(f"Error: {exc}", file=sys.stderr)
			continue
		history.append({"role": "assistant", "content": reply})
		while len(history) > 1 + 2 * MAX_HISTORY_TURNS:
			del history[1:3]
		print(f"\nAI: {reply}")


if __name__ == "__main__":
	raise SystemExit(main())
