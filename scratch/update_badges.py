import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Define brand colors for logos
brand_colors = {
    'python': '3776AB',
    'html5': 'E34F26',
    'css3': '1572B6',
    'javascript': 'F7DF1E',
    'django': '092E20',
    'fastapi': '009688',
    'auth0': 'EB5424',
    'sqlite': '003B57',
    'mysql': '4479A1',
    'mongodb': '47A248',
    'numpy': '013243',
    'pandas': '150458',
    'opencv': '5C3EE8',
    'tensorflow': 'FF6F00',
    'git': 'F05032',
    'github': '181717',
    'visual-studio-code': '007ACC',
    'node.js': '339933',
    'react': '20232A'
}

def replace_badge(match):
    full_match = match.group(0)
    badge_text = match.group(1)
    logo = match.group(2)
    
    color = brand_colors.get(logo.lower(), '8B5CF6') # fallback to purple
    logo_color = 'white'
    if logo.lower() in ['javascript', 'react']:
        # For bright backgrounds, black logo looks better, but wait, react is usually black bg with cyan logo, or just white on dark. Let's stick to white for everything except JS
        if logo.lower() == 'javascript':
            logo_color = 'black'
        else:
            logo_color = '61DAFB' # React cyan
    
    # Reconstruct the badge URL
    return f'https://img.shields.io/badge/{badge_text}-050505?style=for-the-badge&logo={logo}&logoColor={logo_color}&color={color}'

# Regex to find the badge URLs in the tech stack section
# Old: https://img.shields.io/badge/Python-050505?style=for-the-badge&logo=python&logoColor=22D3EE&color=8B5CF6
pattern = r'https://img\.shields\.io/badge/([^?]+)-050505\?style=for-the-badge&logo=([^&]+)&logoColor=22D3EE&color=8B5CF6'
new_content = re.sub(pattern, replace_badge, content)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated badges in README.md")
