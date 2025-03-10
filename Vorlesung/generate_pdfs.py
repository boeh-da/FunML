import re
import os
import subprocess

def insert_print_styles_into_html(filename):
    # CSS styles for print media
    styles = """
<style type="text/css">
@media print {
    /* Adjust the size of h1 headers */
    .slides h1 {
        font-size: 16pt; /* You can adjust this size accordingly */
    }

    /* Adjust the size of h2 headers */
    .slides h2 {
        font-size: 14pt; /* You can adjust this size accordingly */
    }

    /* Continue for h3, h4, etc., if you have them in your presentation. */
}
</style>
"""
    
    # Read the content of the file
    with open(filename, 'r') as file:
        content = file.read()

    # Check if the </head> tag is in the file content
    if '</head>' not in content:
        print("Error: </head> tag not found in the file!")
        return

    # Insert the styles just before the </head> tag
    updated_content = content.replace('</head>', styles + '\n</head>')

    # Write the updated content back to the file
    with open(filename, 'w') as file:
        file.write(updated_content)


def replace_reveal(filename):# Read the file into memory
    with open(filename, 'r') as file:
        content = file.read()

    # Define the new configuration
    new_config = """
    Reveal.initialize({
        controls: true,c
        progress: true,
        history: true,
        transition: "slide",
        plugins: [RevealNotes],
        margin: 0.05,
        minScale: 0.2,
        maxScale: 3.0,
        width: 794,
        height: 1123,
        pdfSeparateFragments: false,
        center: false
    });
    """

    # Replace the old configuration using regex
    content_modified = re.sub(r'Reveal\.initialize\({.*?}\);', new_config, content, flags=re.DOTALL)

    # Write the modified content back to the file
    with open(filename, 'w') as file:
        file.write(content_modified)

def convert_notebook_to_slides(filename):
    cmd = ["jupyter", "nbconvert", "--to", "slides", filename]
    subprocess.run(cmd)

def convert_slides_to_pdf():
    cmd = ["node", "convert.js"]
    subprocess.run(cmd)

def replace_filename_in_js(new_filename):
    # Read the JS file content
    with open('convert.js', 'r') as file:
        lines = file.readlines()

    # Go through each line and replace the filename
    for index, line in enumerate(lines):
        if 'await page.goto(' in line:
            prefix = "await page.goto('file:///Users/dboehnke/Workspaces/20240311_FunML/FunML/Vorlesung/"
            suffix = ".slides.html?print-pdf', {waitUntil: 'networkidle2'});"
            lines[index] = prefix + new_filename + suffix + "\n"
        elif 'await page.pdf({ path:' in line:
            prefix = "await page.pdf({ path: '"
            suffix = ".pdf', format: 'A4', printBackground: true });"
            lines[index] = prefix + new_filename + suffix + "\n"

    # Write the modified content back to the JS file
    with open('convert.js', 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    for filename in os.listdir("./"):
#        print(filename)
        if re.match(r'^\d{2}.*\.ipynb$', filename):
            # Your processing logic here
            convert_notebook_to_slides(filename)
            replace_reveal(filename.replace(".ipynb", ".slides.html"))
            insert_print_styles_into_html(filename.replace(".ipynb", ".slides.html"))
            replace_filename_in_js(filename.split('.')[0])
            convert_slides_to_pdf()

    
