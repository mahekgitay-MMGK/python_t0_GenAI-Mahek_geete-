"""Interactive GenAI chat app using an OpenAI-compatible API.

Set OPENAI_API_KEY in your environment before running this script.
Optional: set OPENAI_MODEL or OPENAI_BASE_URL for a different model/provider.
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
		with urlopen(request, timeout=60) as response:
			result = json.loads(response.read().decode("utf-8"))
		return result["choices"][0]["message"]["content"].strip()
	except HTTPError as exc:
		message = exc.read().decode("utf-8", errors="replace")
		raise RuntimeError(f"API returned HTTP {exc.code}: {message}") from exc
	except (URLError, TimeoutError) as exc:
		raise RuntimeError(f"Unable to connect to the AI service: {exc}") from exc
	except (KeyError, IndexError, json.JSONDecodeError) as exc:
		raise RuntimeError("The AI service returned an invalid response.") from exc


def main():
	if not API_KEY:
		print("Missing API key. Set the OPENAI_API_KEY environment variable.")
		return 1

	history = [{"role": "system", "content": SYSTEM_MESSAGE}]
	print(f"GenAI Chat ({MODEL}) | /reset clears chat | /exit quits")
	while True:
		try:
			text = input("\nYou: ").strip()
		except (EOFError, KeyboardInterrupt):
			print("\nGoodbye!")
			return 0

		if not text:
			continue
		if text.lower() in {"/exit", "/quit"}:
			print("Goodbye!")
			return 0
		if text.lower() == "/reset":
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
		print(f"\nAI: {reply}")


if __name__ == "__main__":
	raise SystemExit(main())
