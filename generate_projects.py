
import os

projects = [
    {
        "name": "The Opal Residence",
        "slug": "opal-residence",
        "location": "DHA Phase 2, Islamabad",
        "desc": "A modern masterpiece featuring open plan living and sustainable design.",
        "cover": "../assets/images/projects/murree_apartments/2.JPG",
        "gallery": [
            "../assets/images/projects/combat_house/2.jpg",
            "../assets/images/projects/house_515/3.jpg",
            "../assets/images/projects/murree_apartments/4.JPG",
            "../assets/images/projects/combat_house/3.jpg"
        ]
    },
    {
        "name": "Cornerstone Villa",
        "slug": "cornerstone-villa",
        "location": "Bahria Town Phase 8, Rawalpindi",
        "desc": "Corner plot luxury villa with panoramic views and premium finishing.",
        "cover": "../assets/images/projects/combat_house/1.jpg",
        "gallery": [
            "../assets/images/projects/combat_house/3.jpg",
            "../assets/images/projects/house_515/1.jpg",
            "../assets/images/projects/murree_apartments/5.JPG",
            "../assets/images/projects/house_515/2.jpg"
        ]
    },
    {
        "name": "Safari Heights",
        "slug": "safari-heights",
        "location": "Safari Valley, Bahria Town",
        "desc": "Elevated living standards with contemporary architecture.",
        "cover": "../assets/images/projects/house_515/1.jpg",
        "gallery": [
            "../assets/images/projects/murree_apartments/6.JPG",
            "../assets/images/projects/combat_house/1.jpg",
            "../assets/images/projects/murree_apartments/3.JPG",
            "../assets/images/projects/combat_house/5.jpg"
        ]
    },
    {
        "name": "Margalla View Mansion",
        "slug": "margalla-mansion",
        "location": "DHA Phase 1, Islamabad",
        "desc": "Classical architecture meeting modern luxury in the heart of DHA.",
        "cover": "../assets/images/projects/murree_apartments/3.JPG",
        "gallery": [
            "../assets/images/projects/house_515/2.jpg",
            "../assets/images/projects/combat_house/4.jpg",
            "../assets/images/projects/murree_apartments/7.JPG",
            "../assets/images/projects/house_515/4.jpg"
        ]
    },
    {
        "name": "Garden City Estate",
        "slug": "garden-city-estate",
        "location": "Bahria Garden City",
        "desc": "Sprawling estate designed for privacy and grandeur.",
        "cover": "../assets/images/projects/combat_house/2.jpg",
        "gallery": [
            "../assets/images/projects/murree_apartments/8.JPG",
            "../assets/images/projects/house_515/3.jpg",
            "../assets/images/projects/combat_house/3.jpg",
            "../assets/images/projects/murree_apartments/2.JPG"
        ]
    },
    {
        "name": "River Wing",
        "slug": "river-wing",
        "location": "Bahria Town Phase 7",
        "desc": "River-facing luxury apartments with bespoke interiors.",
        "cover": "../assets/images/projects/house_515/2.jpg",
        "gallery": [
            "../assets/images/projects/murree_apartments/2.JPG",
            "../assets/images/projects/combat_house/5.jpg",
            "../assets/images/projects/house_515/4.jpg",
            "../assets/images/projects/murree_apartments/9.JPG"
        ]
    },
    {
        "name": "Sector F Villa",
        "slug": "sector-f-villa",
        "location": "DHA Phase 4, Islamabad",
        "desc": "Minimalist design philosophy executed with perfection.",
        "cover": "../assets/images/projects/murree_apartments/4.JPG",
        "gallery": [
            "../assets/images/projects/combat_house/1.jpg",
            "../assets/images/projects/house_515/1.jpg",
            "../assets/images/projects/murree_apartments/2.JPG",
            "../assets/images/projects/combat_house/2.jpg"
        ]
    },
    {
        "name": "Overseas Enclave Retreat",
        "slug": "overseas-retreat",
        "location": "Bahria Phase 8, Overseas Enclave",
        "desc": "Designed for our international clients, offering world-class amenities.",
        "cover": "../assets/images/projects/combat_house/3.jpg",
        "gallery": [
            "../assets/images/projects/murree_apartments/5.JPG",
            "../assets/images/projects/house_515/2.jpg",
            "../assets/images/projects/murree_apartments/9.JPG",
            "../assets/images/projects/combat_house/4.jpg"
        ]
    },
    {
        "name": "Executive Lodges",
        "slug": "executive-lodges",
        "location": "Bahria Town Phase 3",
        "desc": "A community of luxury and comfort.",
        "cover": "../assets/images/projects/house_515/3.jpg",
        "gallery": [
            "../assets/images/projects/combat_house/2.jpg",
            "../assets/images/projects/murree_apartments/3.JPG",
            "../assets/images/projects/house_515/1.jpg",
            "../assets/images/projects/murree_apartments/6.JPG"
        ]
    },
    {
        "name": "Skyline Penthouse",
        "slug": "skyline-penthouse",
        "location": "DHA Phase 2, Islamabad",
        "desc": "Urban luxury living at its finest.",
        "cover": "../assets/images/projects/murree_apartments/5.JPG",
        "gallery": [
            "../assets/images/projects/combat_house/3.jpg",
            "../assets/images/projects/house_515/4.jpg",
            "../assets/images/projects/murree_apartments/1.JPG",
            "../assets/images/projects/combat_house/1.jpg"
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | Combat Services</title>
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
            <img src="{cover}" alt="{name} Cover"
                class="project-hero-img">
            <div class="hero-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);"></div>
            <div class="container project-hero-content">
                <h1 class="hero-title">{name}</h1>
                <p class="hero-subtitle">{location}</p>
            </div>
        </section>

        <!-- Project Info & Gallery -->
        <section class="py-large container">
            <div class="two-col-grid" style="align-items: start; margin-bottom: var(--spacing-lg);">
                <div>
                    <h2 class="section-title">Project Vision</h2>
                    <p style="color: var(--color-text-muted); margin-top: 1rem;">
                        {desc} Built with the signature Combat Services discipline.
                    </p>
                </div>
                <div
                    style="background: var(--color-bg-secondary); padding: 2rem; border: 1px solid var(--color-border);">
                    <ul style="color: var(--color-text-muted); line-height: 2;">
                        <li><strong style="color: var(--color-white);">Status:</strong> Completed</li>
                        <li><strong style="color: var(--color-white);">Location:</strong> {location}</li>
                        <li><strong style="color: var(--color-white);">Type:</strong> Luxury Residential</li>
                    </ul>
                </div>
            </div>

            <h3 class="section-title text-center">Gallery</h3>
            <p class="text-center" style="color: var(--color-text-muted); margin-bottom: 2rem;">Interior and Exterior Views.</p>
            <div class="project-gallery">
                {gallery_html}
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

# Generate Pages
for p in projects:
    gallery_html = ""
    for img in p["gallery"]:
        gallery_html += f'<div class="gallery-item"><img src="{img}" alt="Gallery Image"></div>\n'
    
    content = template.format(
        name=p["name"],
        location=p["location"],
        desc=p["desc"],
        cover=p["cover"],
        gallery_html=gallery_html
    )
    
    with open(f"/Users/muhammadbinwaqas/Desktop/combatbuildersweb222/pages/{p['slug']}.html", "w") as f:
        f.write(content)
    
    # Print the card HTML for easy copy-pasting
    print(f"""
    <!-- {p['name']} -->
    <a href="{p['slug']}.html" class="project-card">
        <img src="{p['cover']}" alt="{p['name']}" class="project-image">
        <div class="project-overlay">
            <div class="project-category">Residential</div>
            <h3 class="project-title">{p['name']}</h3>
            <div class="project-location">{p['location']}</div>
        </div>
    </a>
    """)
