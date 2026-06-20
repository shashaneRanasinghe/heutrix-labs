import os

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replacements for Methodology.jsx and Problem.jsx
    content = content.replace("font-display-md text-display-md-mobile md:text-display-md", "font-headline-md text-headline-md")
    content = content.replace("font-display-sm text-display-sm-mobile md:text-display-sm", "font-headline-md text-headline-md")
    content = content.replace("font-display-sm text-display-sm", "font-headline-md text-headline-md")
    
    # Check if there are other occurrences of display-md or display-sm
    content = content.replace("text-display-md", "text-headline-md")
    content = content.replace("text-display-sm", "text-headline-md")

    with open(filepath, 'w') as f:
        f.write(content)

replace_in_file('src/components/Problem.jsx')
replace_in_file('src/components/Methodology.jsx')
replace_in_file('src/components/Services.jsx')
replace_in_file('src/components/Hero.jsx')

