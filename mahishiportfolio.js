// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const href = this.getAttribute('href');
        
        // Handle scroll to top
        if (href === '#') {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            return;
        }
        
        const target = document.querySelector(href);
        if (target) {
            const navHeight = document.querySelector('.nav').offsetHeight;
            const targetPosition = target.offsetTop - navHeight - 20;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Active navigation link highlighting
const sections = document.querySelectorAll('.section, .hero');
const navLinks = document.querySelectorAll('.nav-link');

function highlightActiveSection() {
    let current = '';
    const scrollPosition = window.pageYOffset + 150;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            current = section.getAttribute('id') || 'about';
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}

window.addEventListener('scroll', highlightActiveSection);
highlightActiveSection(); // Initial call

// Modern Scroll-Driven Animations with Fallback
document.addEventListener('DOMContentLoaded', () => {
    const supportsScrollTimeline = CSS.supports('(animation-timeline: scroll()) and (animation-range: 0% 100%)');
    const animatedElements = document.querySelectorAll(
        '.skill-item, .timeline-item, .project-card, .education-item, .contact-link'
    );
    
    if (!supportsScrollTimeline) {
        // Fallback: Continuous IntersectionObserver for smooth scrubbed animation
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                const ratio = entry.intersectionRatio;
                // Reveal fully when 30% of the element is visible
                const progress = Math.min(ratio / 0.3, 1);
                
                entry.target.style.opacity = progress;
                entry.target.style.transform = `translateY(${(1 - progress) * 60}px) scale(${0.9 + progress * 0.1})`;
            });
        }, { 
            threshold: Array.from({length: 101}, (_, i) => i / 100),
            rootMargin: '0px 0px -5% 0px'
        });

        animatedElements.forEach(el => {
            el.style.opacity = '0';
            el.style.willChange = 'opacity, transform';
            observer.observe(el);
        });
    } else {
        // Native CSS scroll timeline
        animatedElements.forEach(el => el.classList.add('scroll-reveal-native'));
    }
});

// Add active state styling for nav links
const style = document.createElement('style');
style.textContent = `
    .nav-link.active {
        color: var(--turquoise);
        text-shadow: 0 0 8px rgba(64, 224, 208, 0.4);
    }
    .nav-link.active::after {
        width: 100%;
    }
`;
document.head.appendChild(style);

