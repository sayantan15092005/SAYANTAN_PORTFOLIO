import re

with open('c:/Users/SAYANTAN MONDAL/OneDrive/Desktop/assignment/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
css_to_add = """
        /* Extra Styles for Mobile, Theme, Stats */
        /* Stats Section */
        #stats {
            background: #f8f9fa;
            padding: 2rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        .stats-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5rem;
        }
        .stat-card {
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .stat-card:hover {
            transform: translateY(-5px);
        }
        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .stat-label {
            font-size: 0.9rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            opacity: 0.9;
        }

        /* Responsive Mobile Nav & Hamburger */
        .hamburger {
            display: none;
            flex-direction: column;
            cursor: pointer;
            gap: 5px;
            background: transparent;
            border: none;
            z-index: 2000;
        }
        .hamburger span {
            width: 25px;
            height: 3px;
            background: white;
            transition: 0.3s;
            border-radius: 3px;
        }
        .theme-btn {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.3s;
        }
        .theme-btn:hover { background: rgba(255, 255, 255, 0.4); }

        /* Dark Theme overrides */
        body.dark-theme { background-color: #121212; color: #e0e0e0; }
        body.dark-theme #about, body.dark-theme #projects, body.dark-theme #contact, body.dark-theme .coursework-section, body.dark-theme #stats { background-color: #1a1a1a !important; }
        body.dark-theme #skills, body.dark-theme #certificates, body.dark-theme #patents { background-color: #121212 !important; }
        
        body.dark-theme section h2, body.dark-theme .about-text h3, body.dark-theme .project-card h3, body.dark-theme .certificate-card h4, body.dark-theme .skill-category h4, body.dark-theme .coursework-section h4, body.dark-theme .contact-info h3, body.dark-theme .contact-item-content h4, body.dark-theme .form-group label, body.dark-theme .certificate-modal-header h3 { color: #f0f0f0; }
        body.dark-theme p, body.dark-theme .project-features ul, body.dark-theme .about-text p, body.dark-theme .project-card p, body.dark-theme .certificate-card p, body.dark-theme .form-group input, body.dark-theme .form-group textarea { color: #cccccc; }
        body.dark-theme .section-subtitle, body.dark-theme .project-meta, body.dark-theme .cert-issuer, body.dark-theme .contact-item-content p { color: #aaaaaa; }
        
        body.dark-theme .project-card, body.dark-theme .certificate-card, body.dark-theme .about-box, body.dark-theme .skill-category, body.dark-theme .contact-form, body.dark-theme .certificate-modal-content { background: #242424; box-shadow: 0 5px 15px rgba(0,0,0,0.5); border-left-color: #4da8da; border-top-color: #4da8da; }
        
        body.dark-theme .project-tag, body.dark-theme .cert-badge, body.dark-theme .skill-tag { background: #333333; color: #64ffda; }
        body.dark-theme .form-group input, body.dark-theme .form-group textarea { background: #333333; border-color: #444444; color: #ffffff; }
        body.dark-theme .coursework-item { background: #333333; border-color: #64ffda; color: #64ffda; }
        
        body.dark-theme header { background: #1f1f1f; box-shadow: 0 2px 10px rgba(0,0,0,0.5); }
        body.dark-theme footer { background: #1a1a1a; }
        body.dark-theme .certificate-modal-header { border-bottom-color: #444444; }
        body.dark-theme .stat-card { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); }
        body.dark-theme .project-card::before { background: rgba(77, 168, 218, 0.05); }

        @media (max-width: 768px) {
            .hamburger { display: flex; }
            .nav-links {
                position: fixed;
                right: -100%;
                top: 0;
                flex-direction: column;
                background-color: #2c3e50;
                width: 70%;
                height: 100vh;
                justify-content: center;
                transition: right 0.3s ease;
                z-index: 1000;
            }
            .nav-links.active { right: 0; }
            body.dark-theme .nav-links { background-color: #1f1f1f; }
            .stats-container { grid-template-columns: repeat(2, 1fr); }
            
            #hero { padding: 0 2rem; }
            .hero-content h1 { font-size: 3rem; }
            .hero-profile { width: 200px; height: 200px; }
            .ml-badge { top: 20px; right: 0px; }
            .da-badge { bottom: 20px; left: 0px; }
        }
        @media (max-width: 480px) {
            .stats-container { grid-template-columns: 1fr; }
            .hero-content h1 { font-size: 2.2rem; }
        }
"""
html = html.replace('</style>', css_to_add + '\n    </style>')

# Remove the old specific mobile nav hiding to prevent conflicts
old_nav_hide = """.nav-links {
                display: none;
            }"""
new_nav_hide = """/* nav-links handled by new responsive rules */
            .nav-links {
                /* display: none; */
            }"""
html = html.replace(old_nav_hide, new_nav_hide)

# 2. Update Nav Bar HTML
new_nav = """        <nav>
            <div class="logo">Sayantan Mondal</div>
            <button class="hamburger" onclick="toggleMenu()" title="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-links" id="navLinks">
                <li><a href="#hero">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#patents">Research</a></li>
                <li><a href="#certificates">Certificates</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><button onclick="toggleTheme()" id="themeBtn" class="theme-btn" title="Toggle Dark/Light Mode">🌙</button></li>
            </ul>
        </nav>"""
old_nav_pattern = r'<nav>.*?</nav>'
html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)

# 3. Add Stats Section
stats_html = """        <!-- Stats Section -->
        <section id="stats">
            <div class="stats-container">
                <div class="stat-card">
                    <div class="stat-number">5+</div>
                    <div class="stat-label">Certificates</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">5+</div>
                    <div class="stat-label">Projects</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">2</div>
                    <div class="stat-label">Papers</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">2</div>
                    <div class="stat-label">Patents</div>
                </div>
            </div>
        </section>

        <!-- Projects Section (CSS Grid) -->"""
html = html.replace('<!-- Projects Section (CSS Grid) -->', stats_html)

# 4. Update Patents Section to include Paper Publishing
old_patents_header = "<h2>🏆 Patents</h2>"
new_patents_header = "<h2>🏆 Research & Patents</h2>"
html = html.replace(old_patents_header, new_patents_header)

# Search for the spot to inject paper cards. 
# Look for the last `</div>` inside `#patents` section.
patents_section_end = r'(</div>\s*</section>\s*<!-- Skills Section)'
paper_cards = """
                <div class="certificate-card">
                    <span class="cert-badge" style="background:#3498db; color:white;">Publication</span>
                    <h4>Paper Publishing 1</h4>
                    <p class="cert-issuer">Research Journal</p>
                    <p class="cert-date">Published: 2025</p>
                    <p>An in-depth research paper outlining methodologies and experimental results in improving ML algorithms for practical applications.</p>
                    <a href="#" class="view-cert-link" onclick="event.preventDefault(); alert('Link to paper to be added soon!')">🔗 View Paper</a>
                </div>

                <div class="certificate-card">
                    <span class="cert-badge" style="background:#3498db; color:white;">Publication</span>
                    <h4>Paper Publishing 2</h4>
                    <p class="cert-issuer">International Conference</p>
                    <p class="cert-date">Published: 2026</p>
                    <p>Exploratory data analysis frameworks and predictive modeling techniques for resolving enterprise scale challenges.</p>
                    <a href="#" class="view-cert-link" onclick="event.preventDefault(); alert('Link to paper to be added soon!')">🔗 View Paper</a>
                </div>
            \\1"""
html = re.sub(patents_section_end, paper_cards, html)

# 5. Add JS functions
js_to_add = """
        // Hamburger Menu Toggle
        function toggleMenu() {
            const navLinks = document.getElementById('navLinks');
            navLinks.classList.toggle('active');
        }

        // Close menu when link is clicked
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                document.getElementById('navLinks').classList.remove('active');
            });
        });

        // Dark/Light Theme Toggle
        function toggleTheme() {
            const body = document.body;
            const themeBtn = document.getElementById('themeBtn');
            body.classList.toggle('dark-theme');
            
            if (body.classList.contains('dark-theme')) {
                localStorage.setItem('theme', 'dark');
                themeBtn.textContent = '☀️';
            } else {
                localStorage.setItem('theme', 'light');
                themeBtn.textContent = '🌙';
            }
        }

        // Check local storage for theme
        window.addEventListener('DOMContentLoaded', () => {
            const savedTheme = localStorage.getItem('theme');
            const themeBtn = document.getElementById('themeBtn');
            if (savedTheme === 'dark') {
                document.body.classList.add('dark-theme');
                if (themeBtn) themeBtn.textContent = '☀️';
            }
        });
"""
html = html.replace('</script>', js_to_add + '\n    </script>')

with open('c:/Users/SAYANTAN MONDAL/OneDrive/Desktop/assignment/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
