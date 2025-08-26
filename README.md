# PDF Merge Tool

A Python tool for merging PDF files with support for selecting specific pages from each document.

## Usage Examples

```
# Merge entire PDFs
python pdf_merge_tool.py doc1.pdf doc2.pdf -o merged.pdf

# Merge selected pages
python pdf_merge_tool.py doc1.pdf:1-2,4 doc2.pdf:3-5 -o selected_pages.pdf

# Mix full and partial
python pdf_merge_tool.py a.pdf:1-2 b.pdf c.pdf:2,4 -o output.pdf
```

## Limitations & Future Work

### Limitations 

#### Page Limit
The tool currently encounters issues when merging PDFs that result in approximately 82 or more pages. This limitation appears as blank pages appearing in the output document.

**Workaround**: For large merges, manually perform additional merging rounds by splitting the operation into smaller batches.

**Root Cause**: The underlying issue appears to be related to memory management or PDF processing library constraints when handling large documents.

### Planned Improvements
- Investigate and fix the root cause of the limitation
- Create a simple GUI