import os

template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Combat Services</title>
    <link
        href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="../assets/css/style.css">
</head>

<body>
    <header class="navbar">
        <div class="container navbar-container">
            <a href="../index.html" class="logo">COMBAT SERVICES</a>
            <nav class="nav-links">
                <a href="../index.html">Home</a>
                <a href="about.html">About Us</a>
                <a href="services.html">Services</a>
                <a href="projects.html" class="active">Projects</a>
                <a href="success-stories.html">Success Stories</a>
                <a href="contact.html">Contact</a>
            </nav>
            <div class="mobile-menu-toggle">☰</div>
        </div>
    </header>

    <main>
        <!-- Project Hero (Cover Image) -->
        <section class="project-detail-hero">
            <img src="../assets/images/projects/{slug}/1.jpeg" alt="{title} Cover" class="project-hero-img"
                onerror="this.src='https://placehold.co/1920x1080/111/FFF?text={title}+Cover'">
            <div class="hero-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);"></div>
            <div class="container project-hero-content">
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">Residential Luxury</p>
            </div>
        </section>

        <!-- Project Info & Gallery -->
        <section class="py-large container">
            <div class="two-col-grid" style="align-items: start; margin-bottom: var(--spacing-lg);">
                <div>
                    <h2 class="section-title">Project Details</h2>
                    <p style="color: var(--color-text-muted); margin-top: 1rem;">
                        {description}
                    </p>
                </div>
                <div
                    style="background: var(--color-bg-secondary); padding: 2rem; border: 1px solid var(--color-border);">
                    <ul style="color: var(--color-text-muted); line-height: 2;">
                        <li><strong style="color: var(--color-white);">Client:</strong> Private</li>
                        <li><strong style="color: var(--color-white);">Location:</strong> {location}</li>
                        <li><strong style="color: var(--color-white);">Scope:</strong> Luxury Construction & Interior</li>
                    </ul>
                </div>
            </div>

            <h3 class="section-title text-center">Gallery</h3>
            <div class="project-gallery">
                <div class="gallery-item"><img src="../assets/images/projects/{slug}/2.jpeg"
                        onerror="this.style.display='none'" alt="Interior View 1"></div>
                <div class="gallery-item"><img src="../assets/images/projects/{slug}/3.jpeg"
                        onerror="this.style.display='none'" alt="Interior View 2"></div>
                <div class="gallery-item"><img src="../assets/images/projects/{slug}/1.jpeg"
                         alt="Exterior View"></div>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container footer-content">
            <div class="footer-brand">
                <h3>COMBAT SERVICES</h3>
                <p>Luxury Construction & Development</p>
            </div>
            <div class="footer-links">
                <a href="../index.html">Home</a>
                <a href="about.html">About</a>
                <a href="services.html">Services</a>
                <a href="projects.html">Projects</a>
                <a href="success-stories.html">Success Stories</a>
                <a href="contact.html">Contact</a>
            </div>
            <div class="footer-contact">
                <p>Bahria Town Phase 8, Islamabad</p>
                <p><a href="mailto:COMBATBUILDERS28@GMAIL.COM" style="color: inherit;">COMBATBUILDERS28@GMAIL.COM</a>
                </p>
            </div>
        </div>
        <div class="footer-bottom text-center">
            <p>&copy; Combat Services. All Rights Reserved.</p>
        </div>
    </footer>
    <script src="../assets/js/main.js"></script>
</body>

</html>
"""

projects = [
    {
        "slug": "dha-phase-2-estate",
        "title": "DHA Phase 2 Estate",
        "location": "DHA Phase 2, Islamabad",
        "description": "A stunning corner house offering a perfect blend of modern architecture and functional design. Featuring spacious residential areas and premium finishes."
    },
    {
        "slug": "dha-designer-residence",
        "title": "Designer Residence",
        "location": "DHA Phase 2, Islamabad",
        "description": "This brand new designer house showcases sophisticated interiors and high-end furnishings, setting a new standard for luxury living in DHA."
    },
    {
        "slug": "modern-corner-villa",
        "title": "Modern Corner Villa",
        "location": "DHA Phase 2, Islamabad",
        "description": "A beautiful designer house featuring contemporary aesthetics, large glass windows, and an open floor plan that maximizes natural light."
    },
    {
        "slug": "south-face-manor",
        "title": "South Face Manor",
        "location": "DHA Phase 2 Sector B",
        "description": "An exquisite south-facing property designed for optimal sunlight and ventilation, crafted with attention to detail and luxury materials."
    },
    {
        "slug": "dha-sector-a-villa",
        "title": "DHA Sector A Villa",
        "location": "DHA Phase 4 Sector A",
        "description": "Located in the prestigious Sector A, this 1 Kanal house offers expansive living spaces, lush gardens, and state-of-the-art amenities."
    },
    {
        "slug": "bahria-luxury-estate",
        "title": "Bahria Luxury Estate",
        "location": "Bahria Town Phase 8, Rawalpindi",
        "description": "A magnificent 35 Marla fully furnished house in Bahria Town. This estate represents the pinnacle of opulence with its grand interiors and bespoke furniture."
    },
    {
        "slug": "bahria-phase-7-villa",
        "title": "Bahria Phase 7 Villa",
        "location": "Bahria Town Phase 7, Rawalpindi",
        "description": "A 12 Marla luxury house offering a unique combination of comfort and style, situated in the heart of Bahria Town Phase 7."
    },
    {
        "slug": "safari-executive-villa",
        "title": "Safari Executive Villa",
        "location": "Safari Villas, Bahria Town",
        "description": "An 18 Marla executive-class villa in Safari Villas, featuring classic architectural elements and modern conveniences for a refined lifestyle."
    },
    {
        "slug": "bahria-designer-home",
        "title": "Bahria Designer Home",
        "location": "Bahria Town Phase 8, Rawalpindi",
        "description": "A 10 Marla brand new designer house characterized by its chic facade and smart interior layout, perfect for modern family living."
    }
]

for project in projects:
    filename = f"{project['slug']}.html"
    content = template.format(
        slug=project['slug'],
        title=project['title'],
        location=project['location'],
        description=project['description']
    )
    with open(filename, "w") as f:
        f.write(content)
    print(f"Created {filename}")
