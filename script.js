// ── TRANSLATIONS ──
const translations = {
  ru: {
    // Navbar
    'nav-portfolio':  'Портфолио',
    'nav-products':   'Изделия',
    'nav-about':      'О нас',
    'nav-services':   'Услуги',
    'nav-vacancies':  'Вакансии',
    'nav-contacts':   'Контакты',

    // Hero
    'hero-title':     'Создаём проекты как единое целое',
    'hero-sub':       'Чистая эстетика, продуманные решения и внимание к каждой детали.',
    'hero-btn':       'Оставить заявку',

    // Projects
    'projects-heading':   'Проекты',
    'label-interior':     'Дизайн интерьера',
    'label-products':     'Изделия',
    'label-arch':         'Архитектура',

    // Stats
    'stat-projects':  'Завершённых проектов',
    'stat-years':     'Лет опыта',
    'stat-clients':   'Довольных клиентов',
    'stat-support':   'Поддержка клиентов',

    // Services
    'services-heading':   'Услуги',
    'svc-arch':           'Архитектура',
    'svc-interior':       'Дизайн-проект интерьера',
    'svc-custom':         'Индивидуальные изделия',
    'svc-visual':         'Визуализация',
    'svc-btn':            'Оставить заявку',

    // About
    'about-label':    'О нас',
    'about-title':    'Мы создаём эмоции через дизайн',
    'about-desc':     '<strong>Mukaab</strong> — это команда опытных архитекторов и дизайнеров, специализирующихся на создании премиальных интерьеров. Каждый проект — это уникальное путешествие от идеи к реальности.',
    'check-1':        'Индивидуальный подход к каждому клиенту',
    'check-2':        'Гарантия качества и сроков выполнения',
    'check-3':        'Использование экологичных материалов',
    'check-4':        'Полный цикл от проектирования до сдачи',

    // Contacts
    'contacts-label':     'Контакты',
    'clabel-phone':       'Телефон',
    'clabel-email':       'Email',
    'clabel-address':     'Адрес',
    'clabel-social':      'Социальные сети',
    'address-val':        'Минск, Беларусь',
    'form-label':         'Оставить заявку',
    'ph-name':            'Имя',
    'ph-phone':           'Телефон',
    'opt-call':           'Позвонить',
    'opt-write':          'Написать',
    'agree-text':         'В соответствии с политикой обработки персональных данных и соответствии <a href="#">политикой конфиденциальности</a>',
    'btn-submit':         'Отправить',

    // Footer
    'footer-copy':    '© 2026 &nbsp;|&nbsp; ООО «Мукааб». УНП: 193790928',
    'footer-policy':  'Политика конфиденциальности',
  },

  en: {
    // Navbar
    'nav-portfolio':  'Portfolio',
    'nav-products':   'Products',
    'nav-about':      'About',
    'nav-services':   'Services',
    'nav-vacancies':  'Careers',
    'nav-contacts':   'Contacts',

    // Hero
    'hero-title':     'We Create Projects as a Unified Whole',
    'hero-sub':       'Pure aesthetics, thoughtful solutions and attention to every detail.',
    'hero-btn':       'Leave a Request',

    // Projects
    'projects-heading':   'Projects',
    'label-interior':     'Interior Design',
    'label-products':     'Products',
    'label-arch':         'Architecture',

    // Stats
    'stat-projects':  'Completed Projects',
    'stat-years':     'Years of Experience',
    'stat-clients':   'Satisfied Clients',
    'stat-support':   'Client Support',

    // Services
    'services-heading':   'Services',
    'svc-arch':           'Architecture',
    'svc-interior':       'Custom Productsn ',
    'svc-custom':         'Interior Design',
    'svc-interior': 'Interior Design',
    'svc-visual': 'Visualization',
    // About
    'about-label':    'About Us',
    'about-title':    'We Create Emotions Through Design',
    'about-desc':     '<strong>Mukaab</strong> is a team of experienced architects and designers specialising in creating premium interiors. Every project is a unique journey from idea to reality.',
    'check-1':        'Individual approach to every client',
    'check-2':        'Quality and deadline guarantee',
    'check-3':        'Use of eco-friendly materials',
    'check-4':        'Full cycle from design to handover',

    // Contacts
    'contacts-label':     'Contacts',
    'clabel-phone':       'Phone',
    'clabel-email':       'Email',
    'clabel-address':     'Address',
    'clabel-social':      'Social Media',
    'address-val':        'Minsk, Belarus',
    'form-label':         'Leave a Request',
    'ph-name':            'Name',
    'ph-phone':           'Phone',
    'opt-call':           'Call me',
    'opt-write':          'Message me',
    'agree-text':         'In accordance with the personal data processing policy and in accordance with the <a href="#">privacy policy</a>',
    'btn-submit':         'Send',

    // Footer
    'footer-copy':    '© 2026 &nbsp;|&nbsp; LLC «Mukaab». Tax ID: 193790928',
    'footer-policy':  'Privacy Policy',
  }
};

// ── APPLY LANGUAGE ──
function applyLang(lang) {
  const t = translations[lang];

  // helper: set innerText safely
  const setText = (sel, key) => {
    const el = document.querySelector(sel);
    if (el && t[key] !== undefined) el.textContent = t[key];
  };
  const setHTML = (sel, key) => {
    const el = document.querySelector(sel);
    if (el && t[key] !== undefined) el.innerHTML = t[key];
  };
  const setAttr = (sel, attr, key) => {
    const el = document.querySelector(sel);
    if (el && t[key] !== undefined) el.setAttribute(attr, t[key]);
  };

  // Navbar
  setText('[data-i18n="nav-portfolio"]',  'nav-portfolio');
  setText('[data-i18n="nav-products"]',   'nav-products');
  setText('[data-i18n="nav-about"]',      'nav-about');
  setText('[data-i18n="nav-services"]',   'nav-services');
  setText('[data-i18n="nav-vacancies"]',  'nav-vacancies');
  setText('[data-i18n="nav-contacts"]',   'nav-contacts');

  // Hero
  setText('[data-i18n="hero-title"]',     'hero-title');
  setText('[data-i18n="hero-sub"]',       'hero-sub');
  setText('[data-i18n="hero-btn"]',       'hero-btn');

  // Projects
  setText('[data-i18n="projects-heading"]', 'projects-heading');
  setText('[data-i18n="label-interior"]', 'label-interior');
  setText('[data-i18n="label-products"]', 'label-products');
  setText('[data-i18n="label-arch"]',     'label-arch');

  // Stats
  setText('[data-i18n="stat-projects"]',  'stat-projects');
  setText('[data-i18n="stat-years"]',     'stat-years');
  setText('[data-i18n="stat-clients"]',   'stat-clients');
  setText('[data-i18n="stat-support"]',   'stat-support');

  // Services
  setText('[data-i18n="services-heading"]', 'services-heading');
  setText('[data-i18n="svc-arch"]',       'svc-arch');
  setText('[data-i18n="svc-interior"]',   'svc-interior');
  setText('[data-i18n="svc-custom"]',     'svc-custom');
  setText('[data-i18n="svc-visual"]',     'svc-visual');
  document.querySelectorAll('[data-i18n="svc-btn"]').forEach(el => el.textContent = t['svc-btn']);

  // About
  setText('[data-i18n="about-label"]',    'about-label');
  setText('[data-i18n="about-title"]',    'about-title');
  setHTML('[data-i18n="about-desc"]',     'about-desc');
  setText('[data-i18n="check-1"]',        'check-1');
  setText('[data-i18n="check-2"]',        'check-2');
  setText('[data-i18n="check-3"]',        'check-3');
  setText('[data-i18n="check-4"]',        'check-4');

  // Contacts
  setText('[data-i18n="contacts-label"]', 'contacts-label');
  setText('[data-i18n="clabel-phone"]',   'clabel-phone');
  setText('[data-i18n="clabel-email"]',   'clabel-email');
  setText('[data-i18n="clabel-address"]', 'clabel-address');
  setText('[data-i18n="clabel-social"]',  'clabel-social');
  setText('[data-i18n="address-val"]',    'address-val');
  setText('[data-i18n="form-label"]',     'form-label');
  setAttr('[data-i18n="ph-name"]',   'placeholder', 'ph-name');
  setAttr('[data-i18n="ph-phone"]',  'placeholder', 'ph-phone');
  setText('[data-i18n="opt-call"]',       'opt-call');
  setText('[data-i18n="opt-write"]',      'opt-write');
  setHTML('[data-i18n="agree-text"]',     'agree-text');
  setText('[data-i18n="btn-submit"]',     'btn-submit');

  // Footer
  setHTML('[data-i18n="footer-copy"]',    'footer-copy');
  setText('[data-i18n="footer-policy"]',  'footer-policy');

  // ── html lang attribute (меняет язык документа) ──
  document.documentElement.lang = lang;

  
}

// ── LANGUAGE SWITCHER ──
function changeLanguage(lang) {
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
  const active = document.querySelector(`.lang-btn[onclick="changeLanguage('${lang}')"]`);
  if (active) active.classList.add('active');
  applyLang(lang);
}

/* NAVBAR SCROLL */

const nav = document.getElementById('navbar');

window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 10);
});
// ── HERO SLIDER ──
let current = 0;
const slides = document.getElementById('heroSlides');
const dots = document.querySelectorAll('.hero-dot');
function goSlide(n) {
  current = n;
  slides.style.transform = 'translateX(-' + (100 / 3 * n) + '%)';
  dots.forEach((d, i) => d.classList.toggle('active', i === n));
}
dots.forEach((dot, i) => dot.addEventListener('click', () => goSlide(i)));
setInterval(() => goSlide((current + 1) % 3), 5000);

// ── INIT ──
applyLang('ru');
/* ── BURGER MENU ── */
const burger = document.getElementById('burger');

const navLeft = document.querySelector('.nav-left');
const navRight = document.querySelector('.nav-right');

burger.addEventListener('click', () => {
  navLeft.classList.toggle('active');
  navRight.classList.toggle('active');
});
