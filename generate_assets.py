import os
import urllib.request
import base64

# Fetch GitHub Avatar and convert to Base64
try:
    req = urllib.request.Request("https://github.com/Milan07xt.png?size=200", headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        avatar_data = response.read()
        avatar_b64 = "data:image/png;base64," + base64.b64encode(avatar_data).decode('utf-8')
except Exception as e:
    print("Error fetching avatar:", e)
    avatar_b64 = "" # fallback if fetch fails

os.makedirs('assets', exist_ok=True)

# Cyberpunk Theme Colors
# Pink: #EC4899
# Yellow: #EAB308
# Cyan: #06B6D4

id_card_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="neon" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EC4899" />
      <stop offset="50%" stop-color="#EAB308" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <clipPath id="circleView">
      <circle cx="645" cy="220" r="75" />
    </clipPath>
    <style>
      .title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 32px; font-weight: bold; fill: #FFFFFF; letter-spacing: 2px; }}
      .subtitle {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 18px; fill: #EAB308; letter-spacing: 4px; }}
      .label {{ font-family: monospace; font-size: 14px; fill: #06B6D4; }}
      .value {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 18px; fill: #FFFFFF; font-weight: bold; }}
      
      @keyframes scan {{
        0% {{ transform: translateX(-800px); opacity: 0; }}
        10% {{ opacity: 0.8; }}
        90% {{ opacity: 0.8; }}
        100% {{ transform: translateX(800px); opacity: 0; }}
      }}
      .scanner {{ animation: scan 4s ease-in-out infinite; }}
      
      @keyframes pulse {{
        0% {{ r: 5; opacity: 1; fill: #EC4899; }}
        50% {{ r: 9; opacity: 0.5; fill: #EAB308; }}
        100% {{ r: 5; opacity: 1; fill: #EC4899; }}
      }}
      .status-dot {{ animation: pulse 2s infinite; }}
    </style>
  </defs>

  <rect width="800" height="400" rx="20" fill="url(#bg)" stroke="url(#neon)" stroke-width="3" filter="url(#glow)"/>
  
  <g stroke="rgba(6, 182, 212, 0.15)" stroke-width="1">
    <line x1="0" y1="50" x2="800" y2="50" />
    <line x1="0" y1="100" x2="800" y2="100" />
    <line x1="0" y1="150" x2="800" y2="150" />
    <line x1="0" y1="200" x2="800" y2="200" />
    <line x1="0" y1="250" x2="800" y2="250" />
    <line x1="0" y1="300" x2="800" y2="300" />
    <line x1="0" y1="350" x2="800" y2="350" />
    <line x1="100" y1="0" x2="100" y2="400" />
    <line x1="200" y1="0" x2="200" y2="400" />
    <line x1="300" y1="0" x2="300" y2="400" />
    <line x1="400" y1="0" x2="400" y2="400" />
    <line x1="500" y1="0" x2="500" y2="400" />
    <line x1="600" y1="0" x2="600" y2="400" />
    <line x1="700" y1="0" x2="700" y2="400" />
  </g>

  <rect x="40" y="40" width="450" height="320" rx="15" fill="rgba(234, 179, 8, 0.05)" stroke="rgba(236, 72, 153, 0.3)" stroke-width="1"/>
  
  <text x="70" y="90" class="title">MILAN RATHOD</text>
  <text x="70" y="120" class="subtitle">PYTHON DEVELOPER</text>
  
  <text x="70" y="170" class="label">USERNAME:</text>
  <text x="70" y="195" class="value">@Milan07xt</text>
  
  <text x="70" y="235" class="label">EDUCATION:</text>
  <text x="70" y="260" class="value">B.Sc. Information Technology</text>
  
  <text x="70" y="300" class="label">FOCUS:</text>
  <text x="70" y="325" class="value">Backend • REST APIs • AI/ML</text>
  
  <circle cx="530" cy="70" r="5" fill="#EC4899" class="status-dot" filter="url(#glow)"/>
  <text x="550" y="75" class="label" fill="#EAB308" font-family="'Segoe UI', sans-serif">SYSTEM ONLINE</text>

  <rect x="530" y="120" width="230" height="230" rx="10" fill="rgba(6, 182, 212, 0.05)" stroke="#EC4899" stroke-dasharray="5,5"/>
  
  <image href="{avatar_b64}" x="570" y="145" width="150" height="150" clip-path="url(#circleView)" />
  <circle cx="645" cy="220" r="75" fill="none" stroke="#EAB308" stroke-width="4" filter="url(#glow)"/>
  
  <text x="645" y="325" font-family="monospace" font-size="16" fill="#06B6D4" text-anchor="middle" letter-spacing="2px">MILAN_RATHOD</text>

  <!-- Horizontal scanner wipe instead of vertical scan -->
  <line x1="0" y1="200" x2="800" y2="200" stroke="#06B6D4" stroke-width="4" class="scanner" filter="url(#glow)"/>
</svg>"""

roadmap_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 200" width="100%" height="100%">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <style>
      .text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #FFFFFF; font-weight: bold; text-anchor: middle; }
      @keyframes dash {
        to { stroke-dashoffset: -40; }
      }
      @keyframes pulseNode {
        0% { stroke-width: 2; opacity: 0.8; }
        50% { stroke-width: 6; opacity: 1; }
        100% { stroke-width: 2; opacity: 0.8; }
      }
      .line { stroke: #EC4899; stroke-width: 3; stroke-dasharray: 10, 10; animation: dash 1s linear infinite reverse; }
      .node-anim { animation: pulseNode 1.5s infinite; }
    </style>
  </defs>

  <line x1="100" y1="100" x2="900" y2="100" class="line" filter="url(#glow)"/>

  <g transform="translate(100, 100)">
    <circle cx="0" cy="0" r="15" fill="#0f172a" stroke="#06B6D4" stroke-width="4" filter="url(#glow)" class="node-anim"/>
    <text x="0" y="-25" class="text">Python</text>
  </g>
  <g transform="translate(260, 100)">
    <circle cx="0" cy="0" r="15" fill="#0f172a" stroke="#EAB308" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="35" class="text">Data Analysis</text>
  </g>
  <g transform="translate(420, 100)">
    <circle cx="0" cy="0" r="15" fill="#0f172a" stroke="#EC4899" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="-25" class="text">Machine Learning</text>
  </g>
  <g transform="translate(580, 100)">
    <circle cx="0" cy="0" r="15" fill="#0f172a" stroke="#06B6D4" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="35" class="text">Django REST APIs</text>
  </g>
  <g transform="translate(740, 100)">
    <circle cx="0" cy="0" r="15" fill="#0f172a" stroke="#EAB308" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="-25" class="text">Deployment</text>
  </g>
  <g transform="translate(900, 100)">
    <circle cx="0" cy="0" r="15" fill="#EC4899" filter="url(#glow)" class="node-anim"/>
    <text x="0" y="35" class="text" fill="#EC4899">Real-World Projects</text>
  </g>
</svg>"""

with open('assets/id-card.svg', 'w', encoding='utf-8') as f:
    f.write(id_card_svg)

with open('assets/roadmap.svg', 'w', encoding='utf-8') as f:
    f.write(roadmap_svg)

print("Generated SVGs.")
