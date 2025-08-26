```
# Merge entire PDFs
python pdf_merge_tool.py doc1.pdf doc2.pdf -o merged.pdf

# Merge selected pages
python pdf_merge_tool.py doc1.pdf:1-2,4 doc2.pdf:3-5 -o selected_pages.pdf

# Mix full and partial
python pdf_merge_tool.py a.pdf:1-2 b.pdf c.pdf:2,4 -o output.pdf
```