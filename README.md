<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Milan Rathod - Python Developer | 3D Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f3460 0%, #16213e 50%, #1a1a2e 100%);
            color: #fff;
            overflow-x: hidden;
            line-height: 1.6;
        }
        /* 3D Canvas Section */
        .hero-section {
            position: relative;
            width: 100%;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        #canvas {
            position: absolute;
            top: 0;
            left: 0;
            display: block;
            width: 100%;
            height: 100%;
        }
        .hero-content {
            position: relative;
            z-index: 10;
            text-align: center;
            animation: fadeInDown 1s ease;
       }
        .hero-content h1 {
            font-size: clamp(2.5em, 8vw, 5em);
            margin-bottom: 20px;
            text-shadow: 0 0 30px rgba(57, 211, 83, 0.6);
            color: #39d353;
            letter-spacing: 2px;
            animation: float 3s ease-in-out infinite;
        }
        .hero-content .subtitle {
            font-size: clamp(1.1em, 3vw, 1.5em);
            color: #1f6feb;
            text-shadow: 0 0 20px rgba(31, 111, 235, 0.5);
            margin-bottom: 15px;
            background: linear-gradient(135deg, #39d353, #1f6feb, #39d353);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradient-shift 4s ease infinite;
        }
        .scroll-indicator {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            animation: bounce 2s infinite;
            cursor: pointer;
            z-index: 15;
        }
        .scroll-indicator svg {
            width: 30px;
            height: 30px;
            stroke: #39d353;
            stroke-width: 2;
            fill: none;
        }
        /* Main Content Section */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        section {
            padding: 80px 0;
            animation: fadeInUp 0.8s ease;
        }
 section.dark {
            background: linear-gradient(180deg, rgba(15, 52, 96, 0.5), rgba(26, 26, 46, 0.5));
        }
        h2 {
            font-size: 3em;
            margin-bottom: 50px;
            text-align: center;
            color: #39d353;
            text-shadow: 0 0 20px rgba(57, 211, 83, 0.3);
            position: relative;
            padding-bottom: 20px;
        }
        h2:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 3px;
            background: linear-gradient(90deg, #39d353, #1f6feb);
            border-radius: 2px;
        }
        /* About Section */
        .about-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        .about-card {
            background: rgba(57, 211, 83, 0.1);
            border: 2px solid #39d353;
            padding: 30px;
            border-radius: 10px;
            transition: all 0.3s ease;
            cursor: pointer;
            perspective: 1000px;
        }
    .about-card:hover {
            transform: translateY(-10px) rotateX(5deg);
            background: rgba(57, 211, 83, 0.2);
            box-shadow: 0 20px 40px rgba(57, 211, 83, 0.3);
        }
        .about-card h3 {
            font-size: 1.3em;
            margin-bottom: 15px;
            color: #39d353;
        }
        .about-card p {
            color: rgba(255, 255, 255, 0.8);
            line-height: 1.8;
        }
        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        .project-card {
            position: relative;
            height: 300px;
            perspective: 1200px;
            cursor: pointer;
        }
        .project-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            transition: transform 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            transform-style: preserve-3d;
        }
        .project-card:hover .project-card-inner {
            transform: rotateY(360deg) rotateX(5deg);
        }
        .project-card-face {
            position: absolute;
            width: 100%;
            height: 100%;
            padding: 25px;
            border-radius: 15px;
            backface-visibility: hidden;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            box-shadow: 0 8px 32px rgba(57, 211, 83, 0.3);
        }
        .project-1 {
            background: linear-gradient(135deg, #39d353 0%, #1f6feb 100%);
        }
        .project-2 {
            background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
        }        .project-3 {
            background: linear-gradient(135deg, #A8EDEA 0%, #FED6E3 100%);
            color: #333;
        }
        .project-card-face h3 {
            font-size: 1.5em;
            margin: 15px 0;
        }
        .project-card-face p {
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 15px;
        }
        .project-links {
            display: flex;
            gap: 15px;
            justify-content: center;
            margin-top: auto;
        }
        .project-links a {
            color: inherit;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            border-bottom: 2px solid currentColor;
            padding-bottom: 3px;
        }
        .project-links a:hover {
            transform: translateY(-3px);
            opacity: 0.8;
        }
        /* Tech Stack Section */
        .tech-stack {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 40px;
        }
        .tech-item {
            padding: 15px;
            perspective: 1000px;
            transition: all 0.3s ease;
        }
        .tech-item img {
            width: 60px;
            height: 60px;
            animation: rotate3d 3s linear infinite;
            filter: drop-shadow(0 0 10px rgba(57, 211, 83, 0.3));
            transition: all 0.3s ease;
        }
        .tech-item:hover img {
            transform: scale(1.2) rotateZ(10deg);
            filter: drop-shadow(0 0 20px rgba(57, 211, 83, 0.6));
        }
        /* Stats Section */
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-top: 40px;
            text-align: center;
        }
        .stat-item {
            padding: 20px;
            border-radius: 10px;
            background: rgba(57, 211, 83, 0.1);
            border: 2px solid #39d353;
        }
        .stat-item img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 8px 20px rgba(57, 211, 83, 0.2);
            transition: all 0.3s ease;
        }
        .stat-item img:hover {
            transform: scale(1.05);
            box-shadow: 0 12px 30px rgba(57, 211, 83, 0.4);
        }
        /* Connect Section */
        .connect-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }
        .connect-btn {
            padding: 20px;
            border: 2px solid #39d353;
            background: rgba(57, 211, 83, 0.1);
            border-radius: 10px;
            color: #39d353;
            text-decoration: none;
            font-weight: 600;
            text-align: center;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .connect-btn:hover {
            background: #39d353;
            color: #000;
            transform: scale(1.1) translateY(-5px);
            box-shadow: 0 10px 30px rgba(57, 211, 83, 0.5);
        }
        /* Footer */
        footer {
            text-align: center;
            padding: 40px 0;
            border-top: 2px solid #39d353;
            color: rgba(255, 255, 255, 0.8);
        }
        .quote {
            font-size: 1.3em;
            font-weight: bold;
            color: #39d353;
            text-shadow: 0 0 20px rgba(57, 211, 83, 0.5);
            margin: 20px 0;
        }
        /* Animations */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px) rotateX(-10deg);
            }
            to {
                opacity: 1;
                transform: translateY(0) rotateX(0deg);
            }
        }
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        @keyframes float {
            0%, 100% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-15px);
            }
        }
        @keyframes gradient-shift {
            0%, 100% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
        }
        @keyframes rotate3d {
            0% {
                transform: rotateY(0deg) rotateZ(0deg);
            }
            50% {
                transform: rotateY(180deg) rotateZ(10deg);
            }
            100% {
                transform: rotateY(360deg) rotateZ(0deg);
            }
        }
        @keyframes bounce {
            0%, 100% {
                transform: translateX(-50%) translateY(0);
            }
            50% {
                transform: translateX(-50%) translateY(10px);
            }
        }
        /* Responsive */
        @media (max-width: 768px) {
            h2 {
                font-size: 2em;
            }
            .hero-content h1 {
                font-size: 2em;
            }
            .hero-content .subtitle {
                font-size: 1.1em;
            }
            section {
                padding: 40px 0;
            }
            .tech-item img {
                width: 50px;
                height: 50px;
            }
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Hero Section with 3D Canvas -->
    <div class="hero-section">
        <canvas id="canvas"></canvas>
        <div class="hero-content">
            <h1>Milan Rathod</h1>
            <div class="subtitle">Python Developer | Django Developer | Backend Developer</div>
        </div>
        <div class="scroll-indicator" onclick="scrollToSection('about')">
            <svg viewBox="0 0 24 24">
                <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
        </div>
    </div>
    <!-- About Section -->
    <section id="about" class="dark">
        <div class="container">
            <h2>👨‍💻 About Me</h2>
            <div class="about-grid">
                <div class="about-card">
                    <h3>🎓 Education</h3>
                    <p>B.Sc. Information Technology Graduate from Noble University, Junagadh with CGPA 6.35. Completed Tata Forage Cybersecurity Analyst Job Simulation.</p>
                </div>
                <div class="about-card">
                    <h3>💻 Skills</h3>
                    <p>Python, Django, Django REST Framework, REST APIs, OpenCV, MySQL, SQLite, PostgreSQL, JavaScript, HTML/CSS, Git, GitHub.</p>
                </div>
                <div class="about-card">
                    <h3>🚀 Focus</h3>
                    <p>Passionate about building modern web applications, creating clean architectures, and developing user-friendly interfaces with full-stack technologies.</p>
                </div>
                <div class="about-card">
                    <h3>📍 Location</h3>
                    <p>Based in Junagadh, Gujarat, India. Open to relocation across Gujarat cities (Ahmedabad, Rajkot, Surat, Vadodara, Gandhinagar).</p>
                </div>
                <div class="about-card">
                    <h3>🎯 Goals</h3>
                    <p>Secure entry-level Python Developer role. Build production-ready projects. Contribute to open-source. Master advanced Django & React.</p>
                </div>
                <div class="about-card">
                    <h3>🌱 Learning</h3>
                    <p>Continuously mastering Django REST Framework, React.js, and modern full-stack development practices for scalable applications.</p>
                </div>
            </div>
        </div>
    </section>
    <!-- Projects Section -->
    <section id="projects">
        <div class="container">
            <h2>🚀 Featured Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-card-inner">
                        <div class="project-card-face project-1">
                            <h3>🎯 Face Recognition Attendance</h3>
                            <p>Python • Django • OpenCV • SQLite</p>
                            <p style="font-size: 0.85em; margin-top: 10px;">Intelligent biometric system with real-time face detection and automated attendance logging.</p>
                            <div class="project-links">
                                <a href="https://face-detection-attendance-woad.vercel.app/home/" target="_blank">Live</a>
                                <a href="https://github.com/Milan07xt/SEM-06" target="_blank">Code</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-card-inner">
                        <div class="project-card-face project-2">
                            <h3>🏋️ Gym Management System</h3>
                            <p>Python • Django • MySQL • REST API</p>
                            <p style="font-size: 0.85em; margin-top: 10px;">Complete fitness center platform with member management, scheduling, and billing features.</p>
                            <div class="project-links">
                                <a href="https://django-gym-management-system-websit-one.vercel.app/" target="_blank">Live</a>
                                <a href="https://github.com/Milan07xt/Django-Gym-Management-System-Website" target="_blank">Code</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-card-inner">
                        <div class="project-card-face project-3">
                            <h3>🏨 Hotel Management System</h3>
                            <p>Python • Django • SQLite • REST API</p>
                            <p style="font-size: 0.85em; margin-top: 10px;">Full-featured hospitality platform with room booking, guest management, and billing system.</p>
                            <div class="project-links">
                                <a href="https://hotel-website-project-kappa.vercel.app/" target="_blank">Live</a>
                                <a href="https://github.com/Milan07xt/Hotel-Website-Project" target="_blank">Code</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Tech Stack Section -->
    <section id="tech" class="dark">
        <div class="container">
            <h2>💻 Tech Stack & Tools</h2>
            <div class="tech-stack">
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=python" alt="Python" title="Python">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=django" alt="Django" title="Django">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=html" alt="HTML" title="HTML">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=css" alt="CSS" title="CSS">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=javascript" alt="JavaScript" title="JavaScript">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=react" alt="React" title="React">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=mysql" alt="MySQL" title="MySQL">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=sqlite" alt="SQLite" title="SQLite">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=git" alt="Git" title="Git">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=github" alt="GitHub" title="GitHub">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=vscode" alt="VS Code" title="VS Code">
                </div>
                <div class="tech-item">
                    <img src="https://skillicons.dev/icons?i=postgresql" alt="PostgreSQL" title="PostgreSQL">
                </div>
            </div>
        </div>
    </section>
    <!-- GitHub Stats Section -->
    <section id="stats">
        <div class="container">
            <h2>🔥 GitHub Activity</h2>
            <div class="stats">
                <div class="stat-item">
                    <img src="https://streak-stats.demolab.com?user=Milan07xt&theme=github-dark&hide_border=true" alt="GitHub Streak">
                </div>
                <div class="stat-item">
                    <img src="https://github-readme-activity-graph.vercel.app/graph?username=Milan07xt&theme=github-compact" alt="Contribution Graph">
                </div>
            </div>
        </div>
    </section>
    <!-- Connect Section -->
    <section id="connect" class="dark">
        <div class="container">
            <h2>🌐 Connect With Me</h2>
            <div class="connect-grid">
                <a href="https://milan-portfolio-website.vercel.app/" class="connect-btn" target="_blank">🌐 Portfolio</a>
                <a href="https://github.com/Milan07xt" class="connect-btn" target="_blank">💻 GitHub</a>
                <a href="https://www.linkedin.com/in/milan-rathod07" class="connect-btn" target="_blank">🔗 LinkedIn</a>
                <a href="mailto:rathodmilan216@gmail.com" class="connect-btn">📧 Email</a>
            </div>
            <div style="text-align: center; margin-top: 50px;">
                <p class="quote">💡 "Code. Learn. Build. Grow."</p>
            </div>
        </div>
    </section>p
    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2024 Milan Rathod. All rights reserved. | Passionate about Python & Backend Development</p>
            <p style="margin-top: 10px; font-size: 0.9em; color: #39d353;">✨ Built with 3D animations, React, Three.js & modern web technologies</p>
        </div>
    </footer>
    <!-- Three.js Script -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Scene Setup
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(
            75,
            window.innerWidth / window.innerHeight,
            0.1,
            1000
        );
        const renderer = new THREE.WebGLRenderer({
            canvas: document.getElementById('canvas'),
            antialias: true,
            alpha: true
        });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x000000, 0.1);
        camera.position.z = 5;
        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
        scene.add(ambientLight);
        const pointLight1 = new THREE.PointLight(0x39d353, 1);
        pointLight1.position.set(5, 5, 5);
        scene.add(pointLight1);
        const pointLight2 = new THREE.PointLight(0x1f6feb, 0.8);
        pointLight2.position.set(-5, -5, 5);
        scene.add(pointLight2);
        // Main Cube
        const geometry = new THREE.BoxGeometry(2, 2, 2);
        const material = new THREE.MeshPhongMaterial({
            color: 0x39d353,
            emissive: 0x39d353,
            emissiveIntensity: 0.2,
            shininess: 100
        });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);
        // Wireframe Cube
        const wireframeGeometry = new THREE.BoxGeometry(2.5, 2.5, 2.5);
        const wireframeMaterial = new THREE.MeshPhongMaterial({
            color: 0x1f6feb,
            wireframe: true,
            emissive: 0x1f6feb,
            emissiveIntensity: 0.3
        });
        const wireframeCube = new THREE.Mesh(wireframeGeometry, wireframeMaterial);
        scene.add(wireframeCube);
        // Particles
        const particleCount = 100;
        const particleGeometry = new THREE.BufferGeometry();
        const positions = new Float32Array(particleCount * 3);
        for (let i = 0; i < particleCount * 3; i += 3) {
            positions[i] = (Math.random() - 0.5) * 20;
            positions[i + 1] = (Math.random() - 0.5) * 20;
            positions[i + 2] = (Math.random() - 0.5) * 20;
        }
        particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const particleMaterial = new THREE.PointsMaterial({
            color: 0x39d353,
            size: 0.1,
            sizeAttenuation: true,
            transparent: true,
            opacity: 0.6
        });
        const particles = new THREE.Points(particleGeometry, particleMaterial);
        scene.add(particles);
        // Orbiting Spheres
        const orbitingSpheres = [];
        const sphereCount = 6;
        const orbitRadius = 4;
        for (let i = 0; i < sphereCount; i++) {
            const sphereGeometry = new THREE.SphereGeometry(0.3, 32, 32);
            const sphereMaterial = new THREE.MeshPhongMaterial({
                color: new THREE.Color().setHSL(i / sphereCount, 1, 0.5),
                emissive: new THREE.Color().setHSL(i / sphereCount, 1, 0.3),
                emissiveIntensity: 0.5
            });
            const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
          sphere.userData = {
                angle: (i / sphereCount) * Math.PI * 2,
                radius: orbitRadius,
                speed: 0.003 + (i * 0.0005)
            };
            scene.add(sphere);
            orbitingSpheres.push(sphere);
        }
        // Torus
        const torusGeometry = new THREE.TorusGeometry(3, 0.2, 16, 100);
        const torusMaterial = new THREE.MeshPhongMaterial({
            color: 0x1f6feb,
            emissive: 0x1f6feb,
            emissiveIntensity: 0.2
        });
        const torus = new THREE.Mesh(torusGeometry, torusMaterial);
        torus.rotation.x = 0.5;
        scene.add(torus);
        // Mouse Interaction
        let mouseX = 0;
        let mouseY = 0;
        const targetRotation = { x: 0, y: 0 };
        document.addEventListener('mousemove', (e) => {
            mouseX = (e.clientX / window.innerWidth) * 2 - 1;
            mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
           targetRotation.y = mouseX * Math.PI * 0.5;
            targetRotation.x = mouseY * Math.PI * 0.5;
        });
        // Window Resize
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
        // Animation Loop
        function animate() {
            requestAnimationFrame(animate);
            cube.rotation.x += (targetRotation.x - cube.rotation.x) * 0.05;
            cube.rotation.y += (targetRotation.y - cube.rotation.y) * 0.05;
            wireframeCube.rotation.x -= (targetRotation.x - wireframeCube.rotation.x) * 0.03;
            wireframeCube.rotation.y -= (targetRotation.y - wireframeCube.rotation.y) * 0.03;
            wireframeCube.rotation.z += 0.002;
            torus.rotation.x += 0.003;
            torus.rotation.y += 0.004;
            orbitingSpheres.forEach(sphere => {
                sphere.userData.angle += sphere.userData.speed;
                sphere.position.x = Math.cos(sphere.userData.angle) * sphere.userData.radius;
                sphere.position.y = Math.sin(sphere.userData.angle) * sphere.userData.radius * 0.5;
                sphere.position.z = Math.sin(sphere.userData.angle * 0.5) * sphere.userData.radius * 0.5;
                sphere.rotation.x += 0.01;
                sphere.rotation.y += 0.02;
            });
            const positionAttribute = particles.geometry.getAttribute('position');
            const positionsArray = positionAttribute.array;
            for (let i = 1; i < particleCount * 3; i += 3) {
                positionsArray[i] -= 0.02;
                if (positionsArray[i] < -10) {
                    positionsArray[i] = 10;
                }
            }
            positionAttribute.needsUpdate = true;
            particles.rotation.x += 0.0001;
            particles.rotation.y += 0.0001;
            renderer.render(scene, camera);
        }
        animate();
        // Scroll to Section
        function scrollToSection(sectionId) {
            const section = document.getElementById(sectionId);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        }
    </script>
</body>
</html>
