import os

os.makedirs('assets', exist_ok=True)

id_card_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080B14" />
      <stop offset="100%" stop-color="#050505" />
    </linearGradient>
    <linearGradient id="neon" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" />
      <stop offset="50%" stop-color="#22D3EE" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <style>
      .title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 32px; font-weight: bold; fill: #FFFFFF; letter-spacing: 2px; }
      .subtitle { font-family: 'Segoe UI', Arial, sans-serif; font-size: 18px; fill: #22D3EE; letter-spacing: 4px; }
      .label { font-family: monospace; font-size: 14px; fill: #A855F7; }
      .value { font-family: 'Segoe UI', Arial, sans-serif; font-size: 18px; fill: #FFFFFF; font-weight: bold; }
      
      @keyframes scan {
        0% { transform: translateY(0px); opacity: 0; }
        10% { opacity: 0.5; }
        50% { transform: translateY(350px); opacity: 0.5; }
        90% { opacity: 0.5; }
        100% { transform: translateY(400px); opacity: 0; }
      }
      .scanner { animation: scan 3s linear infinite; }
      
      @keyframes pulse {
        0% { r: 5; opacity: 1; }
        50% { r: 8; opacity: 0.5; }
        100% { r: 5; opacity: 1; }
      }
      .status-dot { animation: pulse 2s infinite; }
    </style>
  </defs>

  <rect width="800" height="400" rx="20" fill="url(#bg)" stroke="url(#neon)" stroke-width="3" filter="url(#glow)"/>
  
  <g stroke="rgba(139, 92, 246, 0.1)" stroke-width="1">
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

  <rect x="40" y="40" width="450" height="320" rx="15" fill="rgba(139, 92, 246, 0.05)" stroke="rgba(34, 211, 238, 0.3)" stroke-width="1"/>
  
  <text x="70" y="90" class="title">MILAN RATHOD</text>
  <text x="70" y="120" class="subtitle">PYTHON DEVELOPER</text>
  
  <text x="70" y="170" class="label">USERNAME:</text>
  <text x="70" y="195" class="value">@Milan07xt</text>
  
  <text x="70" y="235" class="label">EDUCATION:</text>
  <text x="70" y="260" class="value">B.Sc. Information Technology</text>
  
  <text x="70" y="300" class="label">FOCUS:</text>
  <text x="70" y="325" class="value">Backend • REST APIs • AI/ML</text>
  
  <circle cx="530" cy="70" r="5" fill="#22D3EE" class="status-dot" filter="url(#glow)"/>
  <text x="550" y="75" class="label" fill="#22D3EE" font-family="'Segoe UI', sans-serif">OPEN TO OPPORTUNITIES</text>

  <rect x="530" y="120" width="230" height="230" rx="10" fill="rgba(34, 211, 238, 0.05)" stroke="#8B5CF6" stroke-dasharray="5,5"/>
  <text x="645" y="240" font-family="monospace" font-size="60" fill="#8B5CF6" text-anchor="middle" filter="url(#glow)">{ }</text>
  <text x="645" y="260" font-family="monospace" font-size="12" fill="#22D3EE" text-anchor="middle">MILAN_RATHOD</text>

  <line x1="0" y1="0" x2="800" y2="0" stroke="#22D3EE" stroke-width="2" class="scanner" filter="url(#glow)"/>
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
      .line { stroke: #8B5CF6; stroke-width: 3; stroke-dasharray: 10, 10; animation: dash 2s linear infinite; }
    </style>
  </defs>

  <line x1="100" y1="100" x2="900" y2="100" class="line" filter="url(#glow)"/>

  <g transform="translate(100, 100)">
    <circle cx="0" cy="0" r="15" fill="#080B14" stroke="#22D3EE" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="-25" class="text">Python</text>
  </g>
  <g transform="translate(260, 100)">
    <circle cx="0" cy="0" r="15" fill="#080B14" stroke="#8B5CF6" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="35" class="text">Data Analysis</text>
  </g>
  <g transform="translate(420, 100)">
    <circle cx="0" cy="0" r="15" fill="#080B14" stroke="#A855F7" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="-25" class="text">Machine Learning</text>
  </g>
  <g transform="translate(580, 100)">
    <circle cx="0" cy="0" r="15" fill="#080B14" stroke="#22D3EE" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="35" class="text">Django REST APIs</text>
  </g>
  <g transform="translate(740, 100)">
    <circle cx="0" cy="0" r="15" fill="#080B14" stroke="#8B5CF6" stroke-width="4" filter="url(#glow)"/>
    <text x="0" y="-25" class="text">Deployment</text>
  </g>
  <g transform="translate(900, 100)">
    <circle cx="0" cy="0" r="15" fill="#22D3EE" filter="url(#glow)"/>
    <text x="0" y="35" class="text" fill="#22D3EE">Real-World Projects</text>
  </g>
</svg>"""

with open('assets/id-card.svg', 'w', encoding='utf-8') as f:
    f.write(id_card_svg)

with open('assets/roadmap.svg', 'w', encoding='utf-8') as f:
    f.write(roadmap_svg)

print("Generated SVGs.")
