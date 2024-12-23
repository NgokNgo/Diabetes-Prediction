import nbformat
import sys

def convert_cell(cell):
    if cell.cell_type == 'markdown':
        return cell.source
    elif cell.cell_type == 'code':
        code = cell.source
        return f"```{{r}}\n{code}\n```"
    return ""

def convert_notebook(ipynb_path, rmd_path):
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    rmd_content = []
    for cell in nb.cells:
        rmd_content.append(convert_cell(cell))
    
    with open(rmd_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(rmd_content))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert2rmd.py <input.ipynb> <output.Rmd>")
    else:
        ipynb_path = sys.argv[1]
        rmd_path = sys.argv[2]
        convert_notebook(ipynb_path, rmd_path)