import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Define brand colors for logos
brand_colors = {
    'vercel': '000000',
    'linkedin': '0A66C2',
    'github': '181717'
}

def replace_badge(match):
    badge_text = match.group(1)
    logo = match.group(2)
    
    color = brand_colors.get(logo.lower(), '8B5CF6') # fallback to purple
    logo_color = 'white'
    
    # Reconstruct the badge URL to be a single solid block of brand color, just like the tech stack badges.
    return f'https://img.shields.io/badge/{badge_text}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color}'

# Regex to find the badge URLs that have labelColor in them (Top links & Featured Projects)
# Old: https://img.shields.io/badge/PORTFOLIO-050505?style=for-the-badge&logo=vercel&logoColor=22D3EE&labelColor=050505&color=8B5CF6
pattern = r'https://img\.shields\.io/badge/([^?]+)-050505\?style=for-the-badge&logo=([^&]+)&logoColor=22D3EE&labelColor=050505&color=8B5CF6'
new_content = re.sub(pattern, replace_badge, content)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated remaining badges in README.md")
