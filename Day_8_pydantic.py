"""Pydantic theory and a DocumentRecord example.

Pydantic is a Python library for validating and parsing data using type hints.
You define a model by subclassing BaseModel and declaring its fields. When a
model is instantiated, Pydantic checks the input, converts compatible values
to the declared types, and raises ValidationError when data is invalid.
Models can be exported with model_dump() or model_dump_json(), and can produce
JSON Schema for sharing their data requirements with other applications.

DocumentRecord is an example of a model for document data. Field can add
constraints and descriptions; default_factory creates a new list for each
record, avoiding a shared mutable default.

Example:
	record = DocumentRecord(document_id="doc-1", title="Notes", content="Text")
	print(record.model_dump())
"""


from pydantic import BaseModel, Field  # type: ignore[import-not-found]


class DocumentRecord(BaseModel):
    file_hash: str = Field(..., min_length=64, max_length=64, description="sha256 hash")
    file_size: int = Field(..., gt=0, description="Greater than zero")
    file_name: str = Field(..., min_length=1, description="More than one character")

from Day_8_pydantic import DocumentRecord

good=DocumentRecord(file_hash="2cf24",file_size=100,file_name="resume.pdf")
print(good)

