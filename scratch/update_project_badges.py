import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace LIVE_DEMO black badges with Cyan badges
content = re.sub(
    r'https://img\.shields\.io/badge/LIVE_DEMO-000000\?style=for-the-badge&logo=vercel&logoColor=white',
    r'https://img.shields.io/badge/LIVE_DEMO-06B6D4?style=for-the-badge&logo=vercel&logoColor=black',
    content
)

# Replace GITHUB black badges in the projects section with SOURCE_CODE purple badges
# Wait, I should only target the ones in the projects section, or just all GITHUB-181717?
# The user said "live demo and code". The top link is also GITHUB-181717 but it's for their profile, not code.
# Let's target the exact lines by replacing the GITHUB badge that comes right after a LIVE_DEMO badge.
# Actually, I can just do a regex that finds the LIVE_DEMO line and the next line.
# Or simpler:
content = re.sub(
    r'https://img\.shields\.io/badge/GITHUB-181717\?style=for-the-badge&logo=github&logoColor=white(.*?</a>\s*</p>\s*</td>)',
    r'https://img.shields.io/badge/SOURCE_CODE-8B5CF6?style=for-the-badge&logo=github&logoColor=white\1',
    content,
    flags=re.DOTALL
)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Live Demo and Code badges")
