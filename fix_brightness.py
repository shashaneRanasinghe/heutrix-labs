with open('src/components/Methodology.jsx', 'r') as f:
    content = f.read()

# Replace the dark text color with a bright legible color in the Safe AI section
content = content.replace("text-on-primary-fixed-variant", "text-inverse-on-surface")

with open('src/components/Methodology.jsx', 'w') as f:
    f.write(content)

