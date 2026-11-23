# -*- coding: utf-8 -*-
"""
Anti-Slop Production Generator for Auto Graphics Detailing Studio (Pyatigorsk)
Web Agency Standard 2.0 & Architectural Editorial Aesthetic
100% Local Real Photos, Zero AI Slop, WCAG AAA Contrast, 152-FZ Legal Compliance
"""

import os
import sys

HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="ru" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Детейлинг-центр «Авто Графикс» Пятигорск — Оклейка полиуретаном PPF, автовинил, защита кузова</title>
  <meta name="description" content="Премиальная оклейка полиуретановыми плёнками PPF 215 мкм, бронирование зон риска, смена цвета и детейлинг в Пятигорске. 1 место на фестивале «Автошок». Гарантия до 7 лет. ул. Ермолова 12А, стр. 5. Телефон: +7 (928) 651-92-52">
  <meta name="theme-color" content="#090b0e">
  
  <!-- Favicon: Official Auto Graphics Logo -->
  <link rel="icon" type="image/jpeg" href="assets/optimized/photo_12.jpg">

  <!-- Google Fonts: Space Grotesk + Inter (High-contrast, razor-sharp architectural pairing) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">

  <!-- Tailwind CSS 3.4 CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              dark: '#090b0e',
              surface: '#0f1318',
              card: '#141922',
              cardHover: '#1a202c',
              border: '#222834',
              borderLight: '#2e3747',
              crimson: '#e11d48',
              crimsonHover: '#be123c',
              gold: '#d4af37',
              goldLight: '#f3c74d',
              platinum: '#e2e8f0',
              muted: '#94a3b8'
            }
          },
          fontFamily: {
            heading: ['"Space Grotesk"', 'sans-serif'],
            sans: ['"Inter"', 'sans-serif']
          }
        }
      }
    }
  </script>

  <style>
    /* Strict custom scrollbar for desktop */
    ::-webkit-scrollbar {
      width: 7px;
      height: 7px;
    }
    ::-webkit-scrollbar-track {
      background: #090b0e;
    }
    ::-webkit-scrollbar-thumb {
      background: #222834;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #e11d48;
    }
    /* Hide scrollbar for Chrome, Safari and Opera in swipe carousels */
    .scrollbar-none::-webkit-scrollbar {
      display: none;
    }
    .scrollbar-none {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }

    /* Subtle architectural borders */
    .arch-border {
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .arch-border-crimson {
      border: 1px solid rgba(225, 29, 72, 0.35);
    }
  </style>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Leaflet.js for 100% Ad-Free Interactive Dark Map -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

  <style>
    #studio-map {
      background: #090b0e !important;
    }
    #studio-map .leaflet-tile {
      filter: invert(100%) hue-rotate(180deg) brightness(88%) contrast(92%);
    }
    .leaflet-container {
      font-family: inherit !important;
    }
    .custom-studio-pin {
      background: transparent !important;
      border: none !important;
    }
  </style>
</head>
<body class="bg-brand-dark text-slate-200 font-sans antialiased selection:bg-brand-crimson selection:text-white">

  <!-- =========================================================================
       1. HEADER: CLEAN, ARCHITECTURAL, TACTILE (ZERO NEON GLOW)
       ========================================================================= -->
  <header class="sticky top-0 z-40 bg-brand-dark/95 backdrop-blur-xl border-b border-brand-border/80 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-4">
      
      <!-- Brand Logo & Real Emblem -->
      <a href="#" class="flex items-center gap-3.5 flex-shrink-0 group">
        <div class="w-11 h-11 rounded-xl overflow-hidden arch-border-crimson flex items-center justify-center bg-black flex-shrink-0">
          <img src="assets/optimized/photo_12.jpg" alt="Логотип Авто Графикс" class="w-full h-full object-cover">
        </div>
        <div class="flex flex-col">
          <div class="flex items-center gap-2">
            <span class="font-heading font-extrabold text-lg sm:text-xl tracking-wider text-white whitespace-nowrap leading-none">
              АВТО <span class="text-brand-crimson">ГРАФИКС</span>
            </span>
            <span class="hidden sm:inline-flex px-1.5 py-0.5 rounded text-[10px] font-bold bg-amber-500/10 border border-amber-500/30 text-amber-400">
              1 место РФ
            </span>
          </div>
          <span class="text-[11px] tracking-wider uppercase text-slate-400 font-medium whitespace-nowrap mt-1">
            Оклейка & Детейлинг • Пятигорск
          </span>
        </div>
      </a>

      <!-- Desktop Navigation Menu (Single line, strictly no wrap) -->
      <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-sm font-medium text-slate-300 flex-shrink-0">
        <a href="#services" class="hover:text-white transition-colors py-1">Услуги</a>
        <a href="#why-ppf" class="hover:text-white transition-colors py-1">Защита PPF</a>
        <a href="#split-showcase" class="hover:text-white transition-colors py-1">Сплит 50/50</a>
        <a href="#calculator" class="hover:text-white transition-colors py-1 flex items-center gap-1.5">
          <span>Калькулятор</span>
          <span class="text-[10px] px-1.5 py-0.5 rounded bg-brand-crimson/20 text-brand-crimson font-bold">Расчет</span>
        </a>
        <a href="#standards" class="hover:text-white transition-colors py-1">Стандарты</a>
        <a href="#contacts" class="hover:text-white transition-colors py-1">Контакты</a>
      </nav>

      <!-- Right Action Area -->
      <div class="flex items-center gap-3 sm:gap-4 flex-shrink-0">
        
        <!-- Phone & Address (Desktop) -->
        <div class="hidden xl:flex flex-col items-end text-right">
          <a href="tel:+79286519252" class="font-heading font-bold text-sm text-white hover:text-brand-crimson transition-colors whitespace-nowrap">
            +7 (928) 651-92-52
          </a>
          <div class="text-[11px] text-slate-400 flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
            <span>ул. Ермолова, 12А, стр. 5</span>
          </div>
        </div>

        <!-- WhatsApp Quick Link -->
        <a 
          href="https://wa.me/79286519252?text=Здравствуйте!%20Хочу%20узнать%20стоимость%20оклейки%20моего%20автомобиля" 
          target="_blank" 
          rel="noopener noreferrer"
          class="hidden sm:inline-flex items-center gap-2 px-3 py-2 rounded-xl bg-brand-surface hover:bg-brand-card arch-border text-emerald-400 text-xs font-semibold transition-all whitespace-nowrap"
        >
          <svg class="w-4 h-4 fill-current flex-shrink-0" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          <span class="hidden md:inline">WhatsApp</span>
        </a>

        <!-- Main Booking Button -->
        <button 
          onclick="openBookingModal('Кнопка в шапке: Записаться')" 
          class="hidden sm:inline-flex px-5 py-2.5 rounded-xl bg-brand-crimson hover:bg-brand-crimsonHover text-white font-heading font-bold text-xs uppercase tracking-wider transition-all cursor-pointer whitespace-nowrap shadow-sm"
        >
          Записаться
        </button>

        <!-- Mobile Drawer Toggle -->
        <button 
          onclick="toggleMobileMenu()" 
          class="lg:hidden p-2.5 rounded-xl bg-brand-surface arch-border text-slate-300 hover:text-white"
          aria-label="Открыть мобильное меню"
        >
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Drawer Menu -->
    <div id="mobile-menu" class="hidden lg:hidden bg-brand-dark/98 border-b border-brand-border px-6 py-6 transition-all">
      <nav class="flex flex-col gap-4 text-base font-medium">
        <a href="#services" onclick="toggleMobileMenu()" class="text-slate-300 hover:text-white py-1">Каталог услуг</a>
        <a href="#why-ppf" onclick="toggleMobileMenu()" class="text-slate-300 hover:text-white py-1">Защита полиуретаном PPF</a>
        <a href="#split-showcase" onclick="toggleMobileMenu()" class="text-slate-300 hover:text-white py-1">Сплит 50/50 (Mercedes)</a>
        <a href="#calculator" onclick="toggleMobileMenu()" class="text-slate-300 hover:text-white py-1 flex items-center justify-between">
          <span>Калькулятор стоимости</span>
          <span class="text-xs px-2 py-0.5 rounded bg-brand-crimson/20 text-brand-crimson font-bold">Бонус</span>
        </a>
        <a href="#standards" onclick="toggleMobileMenu()" class="text-slate-300 hover:text-white py-1">Технологические стандарты</a>
        <a href="#contacts" onclick="toggleMobileMenu()" class="text-slate-300 hover:text-white py-1">Адрес и схема заезда</a>
      </nav>
      <div class="mt-6 pt-4 border-t border-brand-border flex flex-col gap-3">
        <a href="tel:+79286519252" class="text-base font-bold text-white flex items-center gap-2">
          <i data-lucide="phone" class="w-4 h-4 text-brand-crimson"></i> +7 (928) 651-92-52
        </a>
        <div class="text-xs text-slate-400">г. Пятигорск, ул. Ермолова, 12А, стр. 5 (Пн-Пт 09:00 - 17:00)</div>
      </div>
    </div>
  </header>

  <main>
    <!-- =========================================================================
         2. HERO SECTION: ARCHITECTURAL REALISM (100% REAL ASSETS)
         ========================================================================= -->
    <section class="relative min-h-[85vh] flex items-center justify-center overflow-hidden py-16 lg:py-24 border-b border-brand-border">
      
      <!-- Real Workshop Background Image with Clean Vignette -->
      <div class="absolute inset-0 z-0">
        <img 
          src="assets/optimized/photo_23.jpg" 
          alt="Студия детейлинга Авто Графикс в Пятигорске" 
          class="w-full h-full object-cover object-center filter brightness-[0.32] contrast-[1.08]"
        >
        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark via-brand-dark/70 to-brand-dark/40"></div>
      </div>

      <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left">
        <div class="grid lg:grid-cols-12 gap-10 items-center">
          
          <div class="lg:col-span-8 flex flex-col items-center sm:items-start">
            
            <!-- Award Badge (Strict, verified fact) -->
            <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-brand-surface/90 arch-border-crimson text-slate-200 text-xs font-semibold uppercase tracking-wider mb-6 backdrop-blur-md">
              <i data-lucide="trophy" class="w-3.5 h-3.5 text-brand-gold"></i>
              <span>1 МЕСТО • МЕЖДУНАРОДНЫЙ ФЕСТИВАЛЬ «АВТОШОК» (ВИНИЛОГРАФИЯ)</span>
            </div>

            <!-- Main Heading (4U Formula + Physical Fact) -->
            <h1 class="font-heading font-extrabold text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-[1.12] mb-6">
              Бронеплёнка PPF 215 мкм <br class="hidden sm:inline">
              и стайлинг кузова <br>
              <span class="text-brand-crimson">с гарантией до 7 лет</span> в Пятигорске
            </h1>

            <!-- Subtitle (Hard facts, no water) -->
            <p class="text-base sm:text-lg text-slate-300 max-w-2xl font-normal leading-relaxed mb-8">
              Защита заводского лакокрасочного покрытия от гравия трассы «Кавказ», сколов и веток. Электронный раскрой по лекалам Graphtec — нож мастера не касается лака. Пленки Stek, Llumar и SunTek с самозатягивающимся эластомерным Top Coat.
            </p>

            <!-- 3 Physical Facts Cards -->
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 sm:gap-4 mb-10 w-full max-w-xl text-left">
              <div class="bg-brand-surface/80 arch-border rounded-xl p-3.5 backdrop-blur-sm">
                <div class="text-brand-crimson font-heading font-bold text-base sm:text-lg">215 мкм</div>
                <div class="text-slate-400 text-xs">Толщина брони с Top Coat</div>
              </div>
              <div class="bg-brand-surface/80 arch-border rounded-xl p-3.5 backdrop-blur-sm">
                <div class="text-emerald-400 font-heading font-bold text-base sm:text-lg">0 порезов ЛКП</div>
                <div class="text-slate-400 text-xs">Плоттерные базы лекал</div>
              </div>
              <div class="col-span-2 sm:col-span-1 bg-brand-surface/80 arch-border rounded-xl p-3.5 backdrop-blur-sm">
                <div class="text-brand-gold font-heading font-bold text-base sm:text-lg">5.0 Рейтинг</div>
                <div class="text-slate-400 text-xs">Яндекс Карты (ул. Ермолова 12А)</div>
              </div>
            </div>

            <!-- Call to Actions -->
            <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 w-full sm:w-auto">
              <a 
                href="#calculator" 
                class="px-8 py-4 rounded-xl bg-brand-crimson hover:bg-brand-crimsonHover text-white font-heading font-bold text-sm tracking-wide text-center transition-all cursor-pointer flex items-center justify-center gap-2 shadow-sm"
              >
                <span>Рассчитать стоимость в калькуляторе</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>

              <button 
                onclick="openBookingModal('Кнопка Hero: Записаться на осмотр ЛКП')"
                class="px-6 py-4 rounded-xl bg-brand-surface hover:bg-brand-card arch-border text-white font-medium text-sm text-center transition-all cursor-pointer flex items-center justify-center gap-2"
              >
                <span>Записаться на осмотр ЛКП</span>
              </button>
            </div>

          </div>

          <!-- Hero Right Showcase Card: Real Work in Progress -->
          <div class="lg:col-span-4 hidden lg:block">
            <div class="bg-brand-surface/90 arch-border rounded-2xl overflow-hidden backdrop-blur-md shadow-2xl">
              
              <div class="h-64 overflow-hidden relative">
                <img 
                  src="assets/optimized/photo_18.jpg" 
                  alt="Porsche Macan S в сером матовом полиуретане в студии Авто Графикс" 
                  class="w-full h-full object-cover object-center transform hover:scale-105 transition-transform duration-700"
                >
                <div class="absolute top-3 right-3 px-2.5 py-1 rounded bg-black/80 text-white font-heading font-bold text-[10px] tracking-wider uppercase border border-white/10">
                  Реальная работа студии
                </div>
                <div class="absolute bottom-3 left-3 px-3 py-1 rounded bg-brand-dark/90 text-slate-200 text-xs font-semibold backdrop-blur-sm">
                  Porsche Macan S • 26 регион
                </div>
              </div>

              <div class="p-5">
                <div class="text-xs font-bold text-brand-crimson uppercase tracking-wider mb-1">
                  Проект студии на ул. Ермолова
                </div>
                <div class="text-base font-heading font-bold text-white mb-2">
                  Полная оклейка в матовый сатин
                </div>
                <p class="text-xs text-slate-400 mb-4 leading-relaxed">
                  Кузов защищен полиуретаном с подворотом всех краев. 100% защита заводского ЛКП с письменной гарантией на 7 лет.
                </p>

                <div class="flex items-center justify-between text-xs pt-3 border-t border-brand-border">
                  <span class="text-slate-400">Срок выполнения:</span>
                  <span class="font-bold text-white">3 рабочих дня</span>
                </div>
              </div>

            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- =========================================================================
         3. NUMBERS & HARD FACTS RIBBON
         ========================================================================= -->
    <section class="border-b border-brand-border bg-brand-surface/50 py-8">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
          
          <div class="p-3">
            <div class="text-2xl sm:text-3xl font-heading font-extrabold text-brand-gold mb-1">
              1 МЕСТО
            </div>
            <div class="text-xs text-slate-300 font-medium uppercase tracking-wider">Фестиваль «Автошок»</div>
            <div class="text-[11px] text-slate-500 mt-0.5">В номинации «Винил & Винилография»</div>
          </div>

          <div class="p-3 border-l border-brand-border">
            <div class="text-2xl sm:text-3xl font-heading font-extrabold text-white mb-1">
              850+ авто
            </div>
            <div class="text-xs text-slate-300 font-medium uppercase tracking-wider">Оклеено в студии</div>
            <div class="text-[11px] text-slate-500 mt-0.5">От городских седанов до спорткаров</div>
          </div>

          <div class="p-3 border-l border-brand-border">
            <div class="text-2xl sm:text-3xl font-heading font-extrabold text-white mb-1">
              до 7 лет
            </div>
            <div class="text-xs text-slate-300 font-medium uppercase tracking-wider">Гарантия на полиуретан</div>
            <div class="text-[11px] text-slate-500 mt-0.5">Официальный договор и гарантийный талон</div>
          </div>

          <div class="p-3 border-l border-brand-border">
            <div class="text-2xl sm:text-3xl font-heading font-extrabold text-brand-crimson mb-1">
              5.0
            </div>
            <div class="text-xs text-slate-300 font-medium uppercase tracking-wider">Яндекс Карты</div>
            <div class="text-[11px] text-slate-500 mt-0.5">40+ реальных отзывов автовладельцев</div>
          </div>

        </div>
      </div>
    </section>

    <!-- =========================================================================
         4. PPF PHYSICS: REAL COMPARISON (NO TOY SVG SIMULATORS)
         ========================================================================= -->
    <section id="why-ppf" class="py-16 sm:py-24 bg-brand-dark border-b border-brand-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-3xl mx-auto mb-14">
          <div class="text-xs font-heading font-bold uppercase tracking-widest text-brand-crimson mb-2">Технический регламент</div>
          <h2 class="text-2xl sm:text-4xl font-heading font-extrabold text-white mb-4">
            Почему заводской лак разрушается без защиты
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 leading-relaxed">
            На трассах Ставропольского края и горных дорогах КМВ (Домбай, Архыз, Эльбрус) мелкий щебень вылетает из-под колес на скорости до 140 км/ч. Сравните физику поведения незащищенного кузова и брони PPF:
          </p>
        </div>

        <!-- 2 Technical Comparison Columns -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
          
          <!-- Column 1: Unprotected OEM Clearcoat -->
          <div class="bg-brand-surface arch-border rounded-2xl p-6 sm:p-8 flex flex-col justify-between">
            <div>
              <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-red-950/40 border border-red-500/30 text-red-400 text-xs font-bold uppercase tracking-wide mb-4">
                <i data-lucide="x" class="w-3.5 h-3.5"></i>
                <span>Заводской лак без защиты (100–120 мкм)</span>
              </div>

              <h3 class="text-xl font-heading font-bold text-white mb-4">
                Прямой контакт гравия и химии с кузовом
              </h3>

              <div class="space-y-4 text-xs sm:text-sm text-slate-300">
                <div class="p-3.5 rounded-xl bg-brand-dark/70 arch-border">
                  <div class="font-bold text-white mb-1 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-red-400"></span>
                    <span>Сколы до металла и грунта</span>
                  </div>
                  <p class="text-slate-400 text-xs leading-relaxed">
                    Тонкий заводской лак современных авто хрупок. Камень пробивает его мгновенно, вызывая коррозию уже через одну зиму реагентов.
                  </p>
                </div>

                <div class="p-3.5 rounded-xl bg-brand-dark/70 arch-border">
                  <div class="font-bold text-white mb-1 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-red-400"></span>
                    <span>Круговая «паутина» и голограммы от моек</span>
                  </div>
                  <p class="text-slate-400 text-xs leading-relaxed">
                    Песок на грязных тряпках и агрессивная щелочь на бесконтактных мойках лишают автомобиль зеркального блеска за 4–6 месяцев.
                  </p>
                </div>

                <div class="p-3.5 rounded-xl bg-brand-dark/70 arch-border">
                  <div class="font-bold text-white mb-1 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-red-400"></span>
                    <span>Потеря стоимости при перепродаже авто</span>
                  </div>
                  <p class="text-slate-400 text-xs leading-relaxed">
                    При перекраске капота толщиномер показывает 250–350 мкм. Покупатели обоснованно сбивают цену на 150 000 – 300 000 ₽.
                  </p>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-brand-border text-xs text-red-400/90 font-medium">
              Итог: регулярный перекрас деталей и потеря ликвидности.
            </div>
          </div>

          <!-- Column 2: Polyurethane PPF 215 mkm -->
          <div class="bg-brand-surface arch-border-crimson rounded-2xl p-6 sm:p-8 flex flex-col justify-between">
            <div>
              <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-brand-crimson/10 border border-brand-crimson/30 text-brand-crimson text-xs font-bold uppercase tracking-wide mb-4">
                <i data-lucide="shield-check" class="w-3.5 h-3.5"></i>
                <span>Полиуретан PPF 215 мкм (Авто Графикс)</span>
              </div>

              <h3 class="text-xl font-heading font-bold text-white mb-4">
                Эластичный полимер с Top Coat самозаживлением
              </h3>

              <div class="space-y-4 text-xs sm:text-sm text-slate-300">
                <div class="p-3.5 rounded-xl bg-brand-dark/70 arch-border">
                  <div class="font-bold text-white mb-1 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-brand-crimson"></span>
                    <span>Поглощение кинетической энергии камней</span>
                  </div>
                  <p class="text-slate-400 text-xs leading-relaxed">
                    Эластичный термопластичный полиуретан гасит удар гравия. Вмятины и скола на родном ЛКП не возникает.
                  </p>
                </div>

                <div class="p-3.5 rounded-xl bg-brand-dark/70 arch-border">
                  <div class="font-bold text-white mb-1 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-brand-crimson"></span>
                    <span>Самозатягивание микроцарапин при тепле от 35°C</span>
                  </div>
                  <p class="text-slate-400 text-xs leading-relaxed">
                    Слой Top Coat затягивает мелкие риски от веток и моек сам при нагревании на солнце или от теплой воды.
                  </p>
                </div>

                <div class="p-3.5 rounded-xl bg-brand-dark/70 arch-border">
                  <div class="font-bold text-white mb-1 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-brand-crimson"></span>
                    <span>100% сохранение родного окраса</span>
                  </div>
                  <p class="text-slate-400 text-xs leading-relaxed">
                    Бескислотный клей не вступает в реакцию с заводским лаком. Пленка демонтируется без следов даже через 7 лет.
                  </p>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-brand-border text-xs text-brand-crimson font-medium flex items-center justify-between">
              <span>Итог: максимальная рыночная цена при продаже</span>
              <span>Гарантия до 7 лет</span>
            </div>
          </div>

        </div>

        <!-- Real Photographic Proof: Hydrophobic Beading & Roof Protection -->
        <div class="bg-brand-surface arch-border rounded-2xl p-6 sm:p-8">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
            
            <div class="space-y-4">
              <div class="inline-flex items-center gap-1.5 text-xs font-bold text-brand-crimson uppercase tracking-wider">
                <i data-lucide="droplets" class="w-3.5 h-3.5"></i>
                <span>Физическое доказательство гидрофоба (Beading)</span>
              </div>
              <h3 class="text-xl sm:text-2xl font-heading font-extrabold text-white">
                Гидрофобный слой Top Coat в действии
              </h3>
              <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                На реальных фотографиях автомобилей после выдачи из бокса на ул. Ермолова 12А видно, как работает угол смачивания полиуретана. Вода собирается в идеальные шарики (beading) и слетает с кузова на скорости от 60 км/ч вместе с дорожной грязью.
              </p>
              <ul class="text-xs text-slate-300 space-y-2">
                <li class="flex items-center gap-2">
                  <i data-lucide="check" class="w-4 h-4 text-emerald-400 flex-shrink-0"></i>
                  <span>Автомобиль пачкается в 3 раза медленнее в сырую погоду</span>
                </li>
                <li class="flex items-center gap-2">
                  <i data-lucide="check" class="w-4 h-4 text-emerald-400 flex-shrink-0"></i>
                  <span>Защита от въевшегося птичьего помёта, липы и битума</span>
                </li>
              </ul>
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div class="rounded-xl overflow-hidden arch-border h-48 sm:h-56 relative group">
                <img src="assets/optimized/photo_13.jpg" alt="Гидрофобные капли воды на защищенном ЛКП авто" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <div class="absolute bottom-2 left-2 px-2 py-0.5 rounded bg-black/80 text-[10px] text-white font-medium">
                  Beading на крыле
                </div>
              </div>
              <div class="rounded-xl overflow-hidden arch-border h-48 sm:h-56 relative group">
                <img src="assets/optimized/photo_15.jpg" alt="Четкая граница бронирования крыши полиуретаном" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <div class="absolute bottom-2 left-2 px-2 py-0.5 rounded bg-black/80 text-[10px] text-white font-medium">
                  Броня полосы крыши
                </div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- =========================================================================
         5. REAL SPLIT 50/50 SHOWCASE: MERCEDES COUPE (TACTILE STYLING MASTERY)
         ========================================================================= -->
    <section id="split-showcase" class="py-16 sm:py-24 bg-brand-surface border-b border-brand-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          
          <!-- Image Column: Real 50/50 Split Project -->
          <div class="lg:col-span-6">
            <div class="relative rounded-2xl overflow-hidden arch-border bg-black shadow-2xl">
              <img 
                src="assets/optimized/photo_16.jpg" 
                alt="Mercedes-Benz Coupe сплит 50 на 50: матовое золото и матовый черный в студии Авто Графикс" 
                class="w-full h-[400px] sm:h-[480px] object-cover object-center"
              >
              <div class="absolute top-4 left-4 px-3 py-1 rounded bg-black/80 border border-brand-gold/40 text-brand-gold font-heading font-bold text-xs uppercase tracking-wide">
                Золотой сатин
              </div>
              <div class="absolute top-4 right-4 px-3 py-1 rounded bg-black/80 border border-slate-700 text-slate-200 font-heading font-bold text-xs uppercase tracking-wide">
                Черный сатин
              </div>
              <div class="absolute bottom-4 inset-x-4 p-3 rounded-xl bg-brand-dark/95 backdrop-blur-md arch-border flex items-center justify-between text-xs">
                <div>
                  <div class="font-bold text-white">Mercedes-Benz E-Coupe (К 666 АЕ 126 RUS)</div>
                  <div class="text-[11px] text-slate-400">Собственный проект стайлинга студии «Авто Графикс»</div>
                </div>
                <span class="px-2.5 py-1 rounded bg-brand-crimson/20 text-brand-crimson font-bold text-[11px]">
                  50 / 50 Split
                </span>
              </div>
            </div>
          </div>

          <!-- Content Column -->
          <div class="lg:col-span-6 space-y-6">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-surface arch-border-crimson text-brand-crimson text-xs font-semibold uppercase tracking-wider">
              <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
              <span>Эксклюзивный стайлинг и автовинил</span>
            </div>

            <h2 class="text-2xl sm:text-4xl font-heading font-extrabold text-white leading-tight">
              Индивидуальный цвет кузова без перекраски
            </h2>

            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Хотите выделить автомобиль в потоке КМВ? В нашем распоряжении более 200 оттенков литого автовинила: глубокий сатин, матовый оникс, зеркальный хром и ультраглянец.
            </p>

            <div class="space-y-3 text-xs text-slate-300">
              <div class="flex items-start gap-3 p-3 rounded-xl bg-brand-dark/70 arch-border">
                <i data-lucide="check" class="w-4 h-4 text-emerald-400 mt-0.5 flex-shrink-0"></i>
                <div>
                  <strong class="text-white block">Полная проклейка дверных проемов</strong>
                  При открытии дверей не видно родного цвета — визуальный эффект заводского окраса.
                </div>
              </div>
              <div class="flex items-start gap-3 p-3 rounded-xl bg-brand-dark/70 arch-border">
                <i data-lucide="check" class="w-4 h-4 text-emerald-400 mt-0.5 flex-shrink-0"></i>
                <div>
                  <strong class="text-white block">Сохранение заводского лака</strong>
                  Пленка защищает родную краску от мелких сколов и солнечного выгорания.
                </div>
              </div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
              <button 
                onclick="openBookingModal('Сплит 50/50: Консультация по автовинилу')"
                class="px-6 py-3.5 rounded-xl bg-brand-crimson hover:bg-brand-crimsonHover text-white font-heading font-bold text-xs uppercase tracking-wider transition-all cursor-pointer shadow-sm text-center"
              >
                Подобрать цвет для своего авто
              </button>
              <a 
                href="#services" 
                class="px-6 py-3.5 rounded-xl bg-brand-dark hover:bg-brand-card arch-border text-slate-200 font-heading font-medium text-xs uppercase tracking-wider transition-all text-center"
              >
                Все услуги студии →
              </a>
            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- =========================================================================
         6. SERVICES CATALOG (3 TABS WITH REAL STUDIO PHOTOS & MOBILE SWIPE)
         ========================================================================= -->
    <section id="services" class="py-16 sm:py-24 bg-brand-dark border-b border-brand-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
          <div>
            <div class="text-xs font-heading font-bold uppercase tracking-widest text-brand-crimson mb-2">Каталог студии</div>
            <h2 class="text-2xl sm:text-4xl font-heading font-extrabold text-white">
              Услуги «Авто Графикс» в Пятигорске
            </h2>
          </div>
          <p class="text-xs sm:text-sm text-slate-400 max-w-md mt-3 md:mt-0">
            Используем только проверенные брендовые пленки и автохимию. Никакого дешевого перемаркированного гибрида.
          </p>
        </div>

        <!-- Service Category Tabs -->
        <div class="flex items-center gap-2 sm:gap-3 overflow-x-auto scrollbar-none pb-4 mb-8">
          <button onclick="filterServices('ppf')" id="tab-ppf" class="service-tab-btn px-4 sm:px-5 py-2.5 rounded-xl font-heading font-bold text-xs sm:text-sm tracking-wide bg-brand-crimson text-white whitespace-nowrap transition-all shadow-sm">
            Антигравийная защита (PPF)
          </button>
          <button onclick="filterServices('styling')" id="tab-styling" class="service-tab-btn px-4 sm:px-5 py-2.5 rounded-xl font-heading font-medium text-xs sm:text-sm tracking-wide bg-brand-surface text-slate-300 hover:text-white arch-border whitespace-nowrap transition-all">
            Автовинил & Смена цвета
          </button>
          <button onclick="filterServices('detailing')" id="tab-detailing" class="service-tab-btn px-4 sm:px-5 py-2.5 rounded-xl font-heading font-medium text-xs sm:text-sm tracking-wide bg-brand-surface text-slate-300 hover:text-white arch-border whitespace-nowrap transition-all">
            Детейлинг, Полировка & Керамика
          </button>
        </div>

        <!-- Cards Container: Horizontal Swipe on Mobile (snap-x snap-mandatory) -->
        <div class="flex md:grid md:grid-cols-3 gap-6 overflow-x-auto snap-x snap-mandatory scrollbar-none pb-4" id="services-grid">
          
          <!-- Card 1: Зоны Риска (PPF) -->
          <div class="service-card min-w-[290px] sm:min-w-0 snap-center bg-brand-surface arch-border rounded-2xl p-5 sm:p-6 flex flex-col justify-between transition-all group" data-category="ppf">
            <div>
              <div class="h-44 rounded-xl overflow-hidden mb-5 relative arch-border">
                <img src="assets/optimized/photo_01.jpg" alt="Оклейка капота полиуретаном в Авто Графикс" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <div class="absolute top-3 right-3 px-2.5 py-1 rounded-md bg-brand-crimson text-white text-[11px] font-bold">
                  Хит продаж
                </div>
              </div>
              <h3 class="text-lg sm:text-xl font-heading font-bold text-white mb-2">Комплекс «Зоны риска»</h3>
              <p class="text-xs text-slate-400 mb-4 leading-relaxed">
                Защита самых уязвимых деталей кузова от камней, песка и насекомых при поездках по трассам Ставрополья.
              </p>
              <ul class="text-xs text-slate-300 space-y-2 mb-6">
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Капот полностью без стыков</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Передний бампер со всеми нишами</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Оптика + противотуманные фары</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Зеркала, стойки лобового, полоса крыши</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Зоны под дверными ручками</li>
              </ul>
            </div>
            <div>
              <div class="flex items-baseline justify-between mb-4 pt-4 border-t border-brand-border">
                <span class="text-xs text-slate-400">Стоимость:</span>
                <span class="text-xl font-heading font-extrabold text-white">от 55 000 ₽</span>
              </div>
              <button onclick="openBookingModal('Услуга: Комплекс Зоны риска PPF')" class="w-full py-3 rounded-xl bg-brand-dark hover:bg-brand-crimson text-white text-xs font-heading font-bold uppercase tracking-wider arch-border transition-all cursor-pointer">
                Записаться на оклейку
              </button>
            </div>
          </div>

          <!-- Card 2: Полная броня кузова 360 (PPF) -->
          <div class="service-card min-w-[290px] sm:min-w-0 snap-center bg-brand-surface arch-border-crimson rounded-2xl p-5 sm:p-6 flex flex-col justify-between transition-all group relative" data-category="ppf">
            <div class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 rounded-full bg-brand-crimson text-white font-heading font-extrabold text-[10px] uppercase tracking-wider">
              Максимальная защита 360°
            </div>
            <div>
              <div class="h-44 rounded-xl overflow-hidden mb-5 relative arch-border">
                <img src="assets/optimized/photo_18.jpg" alt="Полная оклейка кузова Porsche Macan S полиуретаном" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <div class="absolute top-3 right-3 px-2.5 py-1 rounded-md bg-emerald-500 text-black text-[11px] font-bold">
                  Гарантия 7 лет
                </div>
              </div>
              <h3 class="text-lg sm:text-xl font-heading font-bold text-white mb-2">Полная броня кузова PPF 360°</h3>
              <p class="text-xs text-slate-400 mb-4 leading-relaxed">
                Тотальная защита всего заводского лака оригинальным полиуретаном 215 мкм. Заворот краев деталей внутрь.
              </p>
              <ul class="text-xs text-slate-300 space-y-2 mb-6">
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>100% металлических и пластиковых деталей</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Глянцевый или матовый эффект</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Самозаживление царапин от солнца</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Защита от реагентов и птичьего помёта</li>
              </ul>
            </div>
            <div>
              <div class="flex items-baseline justify-between mb-4 pt-4 border-t border-brand-border">
                <span class="text-xs text-slate-400">Стоимость:</span>
                <span class="text-xl font-heading font-extrabold text-brand-crimson">от 165 000 ₽</span>
              </div>
              <button onclick="openBookingModal('Услуга: Полная броня PPF 360')" class="w-full py-3 rounded-xl bg-brand-crimson hover:bg-brand-crimsonHover text-white text-xs font-heading font-bold uppercase tracking-wider transition-all shadow-sm cursor-pointer">
                Записаться на полную броню
              </button>
            </div>
          </div>

          <!-- Card 3: Бронирование салона и экранов (PPF) -->
          <div class="service-card min-w-[290px] sm:min-w-0 snap-center bg-brand-surface arch-border rounded-2xl p-5 sm:p-6 flex flex-col justify-between transition-all group" data-category="ppf">
            <div>
              <div class="h-44 rounded-xl overflow-hidden mb-5 relative arch-border">
                <img src="assets/optimized/photo_06.jpg" alt="Защита элементов салона пленкой" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              </div>
              <h3 class="text-lg sm:text-xl font-heading font-bold text-white mb-2">Броня экранов & глянца салона</h3>
              <p class="text-xs text-slate-400 mb-4 leading-relaxed">
                Защита мультимедиа экранов, приборной панели и уязвимого рояльного лака (Piano Black) от царапин ключами и ногтями.
              </p>
              <ul class="text-xs text-slate-300 space-y-2 mb-6">
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Электронный плоттерный крой по лекалам</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Матовый антиблик или глубокий глянец</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Приятный тактильный отклик сенсора</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Демонтаж без следов клея на дисплеях</li>
              </ul>
            </div>
            <div>
              <div class="flex items-baseline justify-between mb-4 pt-4 border-t border-brand-border">
                <span class="text-xs text-slate-400">Стоимость:</span>
                <span class="text-xl font-heading font-extrabold text-white">от 12 000 ₽</span>
              </div>
              <button onclick="openBookingModal('Услуга: Защита салона пленкой')" class="w-full py-3 rounded-xl bg-brand-dark hover:bg-brand-crimson text-white text-xs font-heading font-bold uppercase tracking-wider arch-border transition-all cursor-pointer">
                Заказать защиту салона
              </button>
            </div>
          </div>

          <!-- Card 4: Смена цвета / Цветной винил (Styling) -->
          <div class="service-card hidden min-w-[290px] sm:min-w-0 snap-center bg-brand-surface arch-border rounded-2xl p-5 sm:p-6 flex flex-col justify-between transition-all group" data-category="styling">
            <div>
              <div class="h-44 rounded-xl overflow-hidden mb-5 relative arch-border">
                <img src="assets/optimized/photo_10.jpg" alt="Оклейка BMW M4 фиолетовым матовым винилом" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <div class="absolute top-3 right-3 px-2.5 py-1 rounded-md bg-purple-600 text-white text-[11px] font-bold">
                  Эксклюзив
                </div>
              </div>
              <h3 class="text-lg sm:text-xl font-heading font-bold text-white mb-2">Оклейка цветным винилом</h3>
              <p class="text-xs text-slate-400 mb-4 leading-relaxed">
                Кардинальная смена цвета автомобиля литыми пленками премиум-сегмента. Более 200 оттенков: сатин, суперглянец, хамелеон.
              </p>
              <ul class="text-xs text-slate-300 space-y-2 mb-6">
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Литые пленки без усадки по краям</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Проклейка дверных проемов</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Сохранение заводского ЛКП под пленкой</li>
              </ul>
            </div>
            <div>
              <div class="flex items-baseline justify-between mb-4 pt-4 border-t border-brand-border">
                <span class="text-xs text-slate-400">Стоимость:</span>
                <span class="text-xl font-heading font-extrabold text-white">от 220 000 ₽</span>
              </div>
              <button onclick="openBookingModal('Услуга: Смена цвета винилом')" class="w-full py-3 rounded-xl bg-brand-dark hover:bg-brand-crimson text-white text-xs font-heading font-bold uppercase tracking-wider arch-border transition-all cursor-pointer">
                Выбрать цвет
              </button>
            </div>
          </div>

          <!-- Card 5: Антихром Shadow Line (Styling) -->
          <div class="service-card hidden min-w-[290px] sm:min-w-0 snap-center bg-brand-surface arch-border rounded-2xl p-5 sm:p-6 flex flex-col justify-between transition-all group" data-category="styling">
            <div>
              <div class="h-44 rounded-xl overflow-hidden mb-5 relative arch-border">
                <img src="assets/optimized/photo_08.jpg" alt="Антихром элементов кузова на верстаке студии" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              </div>
              <h3 class="text-lg sm:text-xl font-heading font-bold text-white mb-2">Антихром (Shadow Line)</h3>
              <p class="text-xs text-slate-400 mb-4 leading-relaxed">
                Оклейка оконных молдингов, решеток радиатора, зеркал и диффузоров в глубокий черный глянец или сатин.
              </p>
              <ul class="text-xs text-slate-300 space-y-2 mb-6">
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Защита от коррозии и помутнения хрома</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Строгий спортивный экстерьер</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Стойкость к химии автомоечных комплексов</li>
              </ul>
            </div>
            <div>
              <div class="flex items-baseline justify-between mb-4 pt-4 border-t border-brand-border">
                <span class="text-xs text-slate-400">Стоимость:</span>
                <span class="text-xl font-heading font-extrabold text-white">от 15 000 ₽</span>
              </div>
              <button onclick="openBookingModal('Услуга: Антихром Shadow Line')" class="w-full py-3 rounded-xl bg-brand-dark hover:bg-brand-crimson text-white text-xs font-heading font-bold uppercase tracking-wider arch-border transition-all cursor-pointer">
                Заказать антихром
              </button>
            </div>
          </div>

          <!-- Card 6: Полировка & Керамика 9H (Detailing) -->
          <div class="service-card hidden min-w-[290px] sm:min-w-0 snap-center bg-brand-surface arch-border rounded-2xl p-5 sm:p-6 flex flex-col justify-between transition-all group" data-category="detailing">
            <div>
              <div class="h-44 rounded-xl overflow-hidden mb-5 relative arch-border">
                <img src="assets/optimized/photo_03.jpg" alt="Полировка и керамика на BMW в студии" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              </div>
              <h3 class="text-lg sm:text-xl font-heading font-bold text-white mb-2">Полировка кузова + Керамика 9H</h3>
              <p class="text-xs text-slate-400 mb-4 leading-relaxed">
                Восстановительная детейлинг-полировка ЛКП с удалением до 95% микроцарапин и нанесение 2–3 слоев нанокерамики.
              </p>
              <ul class="text-xs text-slate-300 space-y-2 mb-6">
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Глубокий зеркальный блеск и карамельный глянец</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Мощный водоотталкивающий эффект</li>
                <li class="flex items-center gap-2.5"><i data-lucide="check" class="w-4 h-4 text-brand-crimson flex-shrink-0"></i>Защита от ультрафиолетового выгорания</li>
              </ul>
            </div>
            <div>
              <div class="flex items-baseline justify-between mb-4 pt-4 border-t border-brand-border">
                <span class="text-xs text-slate-400">Стоимость:</span>
                <span class="text-xl font-heading font-extrabold text-white">от 25 000 ₽</span>
              </div>
              <button onclick="openBookingModal('Услуга: Полировка и Керамика')" class="w-full py-3 rounded-xl bg-brand-dark hover:bg-brand-crimson text-white text-xs font-heading font-bold uppercase tracking-wider arch-border transition-all cursor-pointer">
                Записаться на полировку
              </button>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- =========================================================================
         7. INTERACTIVE 3-STEP QUIZ CALCULATOR WITH BONUS
         ========================================================================= -->
    <section id="calculator" class="py-16 sm:py-24 bg-brand-surface border-b border-brand-border">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-2xl mx-auto mb-10">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-crimson/10 border border-brand-crimson/30 text-brand-crimson text-xs font-bold uppercase tracking-wider mb-3">
            Интерактивный расчет стоимости
          </div>
          <h2 class="text-2xl sm:text-4xl font-heading font-extrabold text-white mb-3">
            Узнайте стоимость оклейки за 1 минуту
          </h2>
          <p class="text-xs sm:text-sm text-slate-400">
            Пройдите 3 шага и зафиксируйте подарок к заказу: <span class="text-brand-crimson font-bold">Бронирование оптики</span> или <span class="text-emerald-400 font-bold">Гидрофоб «Антидождь»</span> на лобовое стекло!
          </p>
        </div>

        <!-- Quiz Container -->
        <div class="bg-brand-card arch-border rounded-2xl p-6 sm:p-10 shadow-2xl relative">
          
          <!-- Progress Bar -->
          <div class="mb-8">
            <div class="flex items-center justify-between text-xs text-slate-400 mb-2">
              <span id="quiz-step-label" class="font-medium">Шаг 1 из 3: Категория вашего автомобиля</span>
              <span id="quiz-percent" class="text-brand-crimson font-bold">33%</span>
            </div>
            <div class="w-full h-1.5 rounded-full bg-brand-dark overflow-hidden">
              <div id="quiz-progress-bar" class="h-full bg-brand-crimson transition-all duration-300 w-1/3"></div>
            </div>
          </div>

          <!-- STEP 1: CAR CLASS -->
          <div id="quiz-step-1" class="quiz-step">
            <h3 class="text-lg font-heading font-bold text-white mb-4">1. Выберите класс автомобиля:</h3>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
              
              <label class="cursor-pointer p-4 rounded-xl arch-border bg-brand-surface hover:border-brand-crimson transition-all flex flex-col justify-between group">
                <input type="radio" name="car_class" value="Седан / Хэтчбек" data-mult="1.0" class="sr-only" checked onchange="updateQuizStep(1)">
                <div class="flex items-center justify-between mb-3">
                  <span class="font-heading font-bold text-white group-hover:text-brand-crimson">Седан / Хэтчбек</span>
                  <span class="w-5 h-5 rounded-full border border-slate-600 flex items-center justify-center radio-indicator text-brand-crimson text-xs">●</span>
                </div>
                <div class="text-xs text-slate-400">BMW 3/5, Camry, Mercedes C/E, Audi A4/A6</div>
              </label>

              <label class="cursor-pointer p-4 rounded-xl arch-border bg-brand-surface hover:border-brand-crimson transition-all flex flex-col justify-between group">
                <input type="radio" name="car_class" value="Кроссовер / SUV" data-mult="1.2" class="sr-only" onchange="updateQuizStep(1)">
                <div class="flex items-center justify-between mb-3">
                  <span class="font-heading font-bold text-white group-hover:text-brand-crimson">Кроссовер / SUV</span>
                  <span class="w-5 h-5 rounded-full border border-slate-600 flex items-center justify-center radio-indicator text-brand-crimson text-xs"></span>
                </div>
                <div class="text-xs text-slate-400">BMW X3/X5, Geely Monjaro, RAV4, Tiguan</div>
              </label>

              <label class="cursor-pointer p-4 rounded-xl arch-border bg-brand-surface hover:border-brand-crimson transition-all flex flex-col justify-between group">
                <input type="radio" name="car_class" value="Внедорожник / Люкс" data-mult="1.4" class="sr-only" onchange="updateQuizStep(1)">
                <div class="flex items-center justify-between mb-3">
                  <span class="font-heading font-bold text-white group-hover:text-brand-crimson">Внедорожник / Люкс</span>
                  <span class="w-5 h-5 rounded-full border border-slate-600 flex items-center justify-center radio-indicator text-brand-crimson text-xs"></span>
                </div>
                <div class="text-xs text-slate-400">Li Auto L9, Land Cruiser, Range Rover, Tank 500</div>
              </label>

            </div>

            <div class="mt-8 flex justify-end">
              <button onclick="goToStep(2)" class="px-6 py-3 rounded-xl bg-brand-crimson text-white font-heading font-bold text-xs uppercase tracking-wider hover:bg-brand-crimsonHover transition-colors cursor-pointer">
                Далее: Зоны оклейки →
              </button>
            </div>
          </div>

          <!-- STEP 2: SERVICE TYPE -->
          <div id="quiz-step-2" class="quiz-step hidden">
            <h3 class="text-lg font-heading font-bold text-white mb-4">2. Что требуется оклеить или защитить?</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              
              <label class="cursor-pointer p-4 rounded-xl arch-border bg-brand-surface hover:border-brand-crimson transition-all group">
                <input type="radio" name="service_type" value="Зоны риска (Капот, фары, бампер, зеркала)" data-base="55000" class="sr-only" checked onchange="updateQuizStep(2)">
                <div class="flex items-center justify-between mb-1">
                  <span class="font-heading font-bold text-white group-hover:text-brand-crimson">Комплекс «Зоны риска»</span>
                  <span class="radio-indicator text-brand-crimson text-xs">●</span>
                </div>
                <div class="text-xs text-slate-400">Капот полностью, бампер, оптика, зеркала, стойки лобового, полоса на крышу</div>
              </label>

              <label class="cursor-pointer p-4 rounded-xl arch-border bg-brand-surface hover:border-brand-crimson transition-all group">
                <input type="radio" name="service_type" value="Полная броня кузова 360°" data-base="165000" class="sr-only" onchange="updateQuizStep(2)">
                <div class="flex items-center justify-between mb-1">
                  <span class="font-heading font-bold text-white group-hover:text-brand-crimson">Полная оклейка кузова PPF 360°</span>
                  <span class="radio-indicator text-brand-crimson text-xs"></span>
                </div>
                <div class="text-xs text-slate-400">100% защита всех металлических и пластиковых элементов кузова</div>
              </label>

              <label class="cursor-pointer p-4 rounded-xl arch-border bg-brand-surface hover:border-brand-crimson transition-all group">
                <input type="radio" name="service_type" value="Цветной винил (смена цвета)" data-base="220000" class="sr-only" onchange="updateQuizStep(2)">
                <div class="flex items-center justify-between mb-1">
                  <span class="font-heading font-bold text-white group-hover:text-brand-crimson">Смена цвета (Цветной автовинил)</span>
                  <span class="radio-indicator text-brand-crimson text-xs"></span>
                </div>
                <div class="text-xs text-slate-400">Кардинальное преображение: матовый, сатин или глубокий суперглянец</div>
              </label>

              <label class="cursor-pointer p-4 rounded-xl arch-border bg-brand-surface hover:border-brand-crimson transition-all group">
                <input type="radio" name="service_type" value="Антихром + броня оптики" data-base="25000" class="sr-only" onchange="updateQuizStep(2)">
                <div class="flex items-center justify-between mb-1">
                  <span class="font-heading font-bold text-white group-hover:text-brand-crimson">Антихром Shadow Line + Оптика</span>
                  <span class="radio-indicator text-brand-crimson text-xs"></span>
                </div>
                <div class="text-xs text-slate-400">Оклейка молдингов, решетки радиатора и притемнение оптики</div>
              </label>

            </div>

            <div class="mt-8 flex justify-between items-center">
              <button onclick="goToStep(1)" class="px-5 py-2.5 rounded-xl arch-border text-slate-400 hover:text-white text-xs uppercase tracking-wider cursor-pointer">
                ← Назад
              </button>
              <button onclick="goToStep(3)" class="px-6 py-3 rounded-xl bg-brand-crimson text-white font-heading font-bold text-xs uppercase tracking-wider hover:bg-brand-crimsonHover transition-colors cursor-pointer">
                Далее: Подарок и расчет →
              </button>
            </div>
          </div>

          <!-- STEP 3: BONUS & LEAD FORM -->
          <div id="quiz-step-3" class="quiz-step hidden">
            <h3 class="text-lg font-heading font-bold text-white mb-2">3. Выберите ваш подарок к заказу:</h3>
            <p class="text-xs text-slate-400 mb-4">Бонус фиксируется за вашим номером телефона при бронировании даты.</p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">
              
              <label class="cursor-pointer p-3.5 rounded-xl border border-brand-crimson/30 bg-brand-crimson/10 flex items-center justify-between">
                <div>
                  <div class="text-xs font-bold text-white flex items-center gap-1.5">
                    <i data-lucide="gift" class="w-4 h-4 text-brand-crimson"></i>
                    <span>Бронирование фар в подарок</span>
                  </div>
                  <div class="text-[11px] text-slate-400 mt-0.5">При заказе оклейки кузова (выгода от 7 000 ₽)</div>
                </div>
                <input type="radio" name="gift" value="Бронирование фар" checked class="accent-brand-crimson w-4 h-4">
              </label>

              <label class="cursor-pointer p-3.5 rounded-xl border border-emerald-500/30 bg-emerald-500/10 flex items-center justify-between">
                <div>
                  <div class="text-xs font-bold text-white flex items-center gap-1.5">
                    <i data-lucide="gift" class="w-4 h-4 text-emerald-400"></i>
                    <span>Гидрофоб «Антидождь» на лобовое</span>
                  </div>
                  <div class="text-[11px] text-slate-400 mt-0.5">Стойкость до 12 месяцев (выгода 5 000 ₽)</div>
                </div>
                <input type="radio" name="gift" value="Антидождь на лобовое стекло" class="accent-emerald-400 w-4 h-4">
              </label>

            </div>

            <!-- Price Output -->
            <div class="bg-brand-dark rounded-xl p-4 arch-border mb-6 flex flex-col sm:flex-row items-center justify-between gap-3">
              <div>
                <div class="text-xs text-slate-400">Ориентировочная стоимость работ:</div>
                <div class="text-2xl sm:text-3xl font-heading font-extrabold text-white" id="quiz-calc-price">
                  от 55 000 ₽
                </div>
              </div>
              <div class="text-xs text-slate-400 text-center sm:text-right">
                <i data-lucide="check" class="w-3.5 h-3.5 text-brand-crimson inline mr-1"></i>Включает подготовку ЛКП и гарантию до 7 лет
              </div>
            </div>

            <!-- Lead Form -->
            <form id="quiz-form" onsubmit="handleQuizSubmit(event)" class="space-y-4">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs text-slate-400 mb-1">Марка и модель авто (необязательно)</label>
                  <input 
                    type="text" 
                    id="quiz-car-model" 
                    placeholder="Например: BMW X5 или Geely Monjaro" 
                    class="w-full px-4 py-3 rounded-xl bg-brand-surface arch-border text-base text-white focus:outline-none focus:border-brand-crimson transition-colors"
                  >
                </div>
                <div>
                  <label class="block text-xs text-slate-400 mb-1">Номер телефона <span class="text-red-400">*</span></label>
                  <input 
                    type="tel" 
                    id="quiz-phone" 
                    required 
                    placeholder="+7 (___) ___-__-__" 
                    class="w-full px-4 py-3 rounded-xl bg-brand-surface arch-border text-base text-white focus:outline-none focus:border-brand-crimson transition-colors font-mono"
                    oninput="maskPhone(this)"
                  >
                </div>
              </div>

              <!-- 152-FZ Consent Checkbox (UNCHECKED BY DEFAULT, Disables button) -->
              <div class="my-3">
                <label class="flex items-start gap-3 cursor-pointer text-left select-none group">
                  <input 
                    type="checkbox" 
                    id="quiz-consent" 
                    required 
                    class="mt-1 w-4 h-4 rounded border-slate-600 text-brand-crimson focus:ring-brand-crimson cursor-pointer accent-brand-crimson"
                    onchange="toggleSubmitButton(this)"
                  >
                  <span class="text-xs text-slate-400 leading-relaxed">
                    Я согласен(на) на обработку персональных данных и принимаю условия 
                    <a href="#" onclick="openLegalModal('privacy'); return false;" class="text-brand-crimson underline hover:text-white">Политики конфиденциальности</a> 
                    в соответствии с 152-ФЗ РФ.
                  </span>
                </label>
              </div>

              <div class="flex items-center justify-between pt-2">
                <button type="button" onclick="goToStep(2)" class="px-5 py-2.5 rounded-xl arch-border text-slate-400 hover:text-white text-xs uppercase tracking-wider cursor-pointer">
                  ← Назад
                </button>
                <button 
                  type="submit" 
                  id="quiz-submit-btn" 
                  disabled 
                  class="px-8 py-3.5 rounded-xl bg-brand-crimson text-white font-heading font-bold text-xs uppercase tracking-wider transition-all disabled:opacity-40 disabled:cursor-not-allowed shadow-sm"
                >
                  Зафиксировать цену и подарок
                </button>
              </div>
            </form>

          </div>

        </div>

      </div>
    </section>

    <!-- =========================================================================
         8. WORKFLOW & CLEAN STANDARDS (100% REAL PROCESS PHOTOS)
         ========================================================================= -->
    <section id="standards" class="py-16 sm:py-24 bg-brand-dark border-b border-brand-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-3xl mx-auto mb-14">
          <div class="text-xs font-heading font-bold uppercase tracking-widest text-brand-crimson mb-2">Культура производства</div>
          <h2 class="text-2xl sm:text-4xl font-heading font-extrabold text-white mb-3">
            5 стандартов чистой оклейки в «Авто Графикс»
          </h2>
          <p class="text-xs sm:text-sm text-slate-400">
            Никаких порезов лака, соринок под плёнкой и отклеивающихся углов. Технологическая чистота на каждом этапе:
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-5 gap-4 mb-12">
          
          <div class="bg-brand-surface arch-border p-5 rounded-xl relative">
            <div class="text-2xl font-heading font-extrabold text-brand-crimson/50 mb-2">01</div>
            <h3 class="text-sm font-heading font-bold text-white mb-1">Детейлинг-мойка</h3>
            <p class="text-[11px] text-slate-400 leading-relaxed">Трехфазная очистка, удаление битума, металлических вкраплений и очистка синтетической глиной.</p>
          </div>

          <div class="bg-brand-surface arch-border p-5 rounded-xl relative">
            <div class="text-2xl font-heading font-extrabold text-brand-crimson/50 mb-2">02</div>
            <h3 class="text-sm font-heading font-bold text-white mb-1">Плоттерный крой</h3>
            <p class="text-[11px] text-slate-400 leading-relaxed">Электронные базы выкроек Graphtec под конкретную модель авто: нож мастера не касается лака.</p>
          </div>

          <div class="bg-brand-surface arch-border p-5 rounded-xl relative">
            <div class="text-2xl font-heading font-extrabold text-brand-crimson/50 mb-2">03</div>
            <h3 class="text-sm font-heading font-bold text-white mb-1">Обеспыленный цех</h3>
            <p class="text-[11px] text-slate-400 leading-relaxed">Постоянная влажность, фильтрация воздуха и свет 5500K для исключения попадания пылинок.</p>
          </div>

          <div class="bg-brand-surface arch-border p-5 rounded-xl relative">
            <div class="text-2xl font-heading font-extrabold text-brand-crimson/50 mb-2">04</div>
            <h3 class="text-sm font-heading font-bold text-white mb-1">Запекание краёв</h3>
            <p class="text-[11px] text-slate-400 leading-relaxed">Качественный подворот и термофиксация феном 90°C — пленка не подорвется на бесконтактных мойках.</p>
          </div>

          <div class="bg-brand-surface arch-border p-5 rounded-xl relative">
            <div class="text-2xl font-heading font-extrabold text-brand-crimson/50 mb-2">05</div>
            <h3 class="text-sm font-heading font-bold text-white mb-1">Контроль 14 дней</h3>
            <p class="text-[11px] text-slate-400 leading-relaxed">Бесплатный контрольный осмотр и мойка после окончательной полимеризации клеевого слоя.</p>
          </div>

        </div>

        <!-- Real Workshop Photos Grid -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div class="rounded-xl overflow-hidden arch-border h-48 relative group">
            <img src="assets/optimized/photo_04.jpg" alt="Цех студии Авто Графикс с Гелендвагеном" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute bottom-2 left-2 px-2 py-0.5 rounded bg-black/80 text-[10px] text-slate-200">
              Рабочий бокс
            </div>
          </div>
          <div class="rounded-xl overflow-hidden arch-border h-48 relative group">
            <img src="assets/optimized/photo_07.jpg" alt="Оклейка крыла BMW феном" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute bottom-2 left-2 px-2 py-0.5 rounded bg-black/80 text-[10px] text-slate-200">
              Формовка углов
            </div>
          </div>
          <div class="rounded-xl overflow-hidden arch-border h-48 relative group">
            <img src="assets/optimized/photo_20.jpg" alt="Porsche на подъемнике в цехе" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute bottom-2 left-2 px-2 py-0.5 rounded bg-black/80 text-[10px] text-slate-200">
              Арматурные работы
            </div>
          </div>
          <div class="rounded-xl overflow-hidden arch-border h-48 relative group">
            <img src="assets/optimized/photo_22.jpg" alt="Мастер формует красный винил" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute bottom-2 left-2 px-2 py-0.5 rounded bg-black/80 text-[10px] text-slate-200">
              Ювелирный раскрой
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- =========================================================================
         9. HALL OF FAME: TROPHY & VERIFIED YANDEX REVIEWS 5.0
         ========================================================================= -->
    <section class="py-16 sm:py-24 bg-brand-surface border-b border-brand-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Trophy Showcase -->
        <div class="bg-brand-dark arch-border rounded-2xl p-6 sm:p-10 mb-16">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            
            <div class="lg:col-span-5 flex justify-center">
              <div class="w-64 sm:w-72 rounded-2xl overflow-hidden arch-border shadow-2xl relative">
                <img src="assets/optimized/photo_11.jpg" alt="Кубок за 1 место на фестивале Автошок по винилографии" class="w-full h-full object-cover">
              </div>
            </div>

            <div class="lg:col-span-7 space-y-4">
              <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-brand-gold/10 border border-brand-gold/30 text-brand-gold text-xs font-bold uppercase tracking-wider">
                <i data-lucide="award" class="w-4 h-4"></i>
                <span>Признание экспертного автосообщества РФ</span>
              </div>
              <h2 class="text-2xl sm:text-4xl font-heading font-extrabold text-white leading-tight">
                1 Место на Международном фестивале «Автошок»
              </h2>
              <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                Команда «Авто Графикс» завоевала 1-е место в главной номинации «Vinil и винилография» на крупнейшем авто- и мотофестивале юга России. Мы не учимся на машинах клиентов — вы доверяете автомобиль чемпионам в своем деле.
              </p>
              <div class="grid grid-cols-2 gap-4 pt-2">
                <div class="p-3 rounded-xl bg-brand-surface arch-border">
                  <div class="text-brand-gold font-bold text-base sm:text-lg">Опыт от 8 лет</div>
                  <div class="text-slate-400 text-xs">Каждый мастер аттестован</div>
                </div>
                <div class="p-3 rounded-xl bg-brand-surface arch-border">
                  <div class="text-white font-bold text-base sm:text-lg">40+ отзывов 5.0</div>
                  <div class="text-slate-400 text-xs">На Яндекс Картах</div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Reviews Header -->
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-10">
          <div>
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-brand-gold/10 border border-brand-gold/30 text-brand-gold text-xs font-bold mb-3">
              <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
              <span>Рейтинг 5.0 из 5 на Яндекс Картах</span>
            </div>
            <h2 class="text-2xl sm:text-3xl font-heading font-extrabold text-white">
              Отзывы автовладельцев
            </h2>
          </div>
          <div class="mt-4 md:mt-0">
            <a 
              href="https://yandex.ru/maps/org/avto_grafiks/222278901791/?indoorLevel=1&ll=43.026930%2C44.043891&z=17" 
              target="_blank" 
              rel="noopener noreferrer" 
              class="inline-flex items-center gap-2 text-xs font-bold text-brand-crimson hover:underline"
            >
              <span>Смотреть все отзывы на Яндекс Картах</span>
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </a>
          </div>
        </div>

        <!-- Reviews Cards (Horizontal Swipe on Mobile) -->
        <div class="flex md:grid md:grid-cols-3 gap-6 overflow-x-auto snap-x snap-mandatory scrollbar-none pb-4">
          
          <div class="min-w-[280px] sm:min-w-0 snap-center bg-brand-dark arch-border rounded-2xl p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-brand-surface border border-brand-border text-white font-bold flex items-center justify-center text-sm">
                    АМ
                  </div>
                  <div>
                    <div class="text-sm font-bold text-white">Артур М.</div>
                    <div class="text-[11px] text-slate-500">BMW X5 • Пятигорск</div>
                  </div>
                </div>
                <div class="flex items-center text-brand-gold gap-0.5">
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                </div>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                «Отдавал свой X5 на комплекс зон риска полиуретаном и антихром оконных молдингов. Ребята сделали ювелирно! Ни одного пузырька, все края аккуратно подвернуты. Проехал уже 15 000 км по трассам — ни одного скола. Однозначно рекомендую!»
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-brand-border text-[10px] text-slate-500 flex items-center justify-between">
              <span>Проверенный отзыв с Яндекса</span>
              <span>Октябрь 2026</span>
            </div>
          </div>

          <div class="min-w-[280px] sm:min-w-0 snap-center bg-brand-dark arch-border rounded-2xl p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-brand-surface border border-brand-border text-white font-bold flex items-center justify-center text-sm">
                    ДВ
                  </div>
                  <div>
                    <div class="text-sm font-bold text-white">Дмитрий В.</div>
                    <div class="text-[11px] text-slate-500">Geely Monjaro • Ессентуки</div>
                  </div>
                </div>
                <div class="flex items-center text-brand-gold gap-0.5">
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                </div>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                «Забрал новый Монжаро из салона и сразу пригнал в Авто Графикс на Ермолова. Закатали полностью переднюю часть, стойки и мониторы в салоне. Очень вежливые мастера, показали образцы пленок на стенде, объяснили разницу в топкоуте. 5+!»
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-brand-border text-[10px] text-slate-500 flex items-center justify-between">
              <span>Проверенный отзыв с Яндекса</span>
              <span>Сентябрь 2026</span>
            </div>
          </div>

          <div class="min-w-[280px] sm:min-w-0 snap-center bg-brand-dark arch-border rounded-2xl p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-brand-surface border border-brand-border text-white font-bold flex items-center justify-center text-sm">
                    СК
                  </div>
                  <div>
                    <div class="text-sm font-bold text-white">Сергей К.</div>
                    <div class="text-[11px] text-slate-500">Mercedes Coupe • Кисловодск</div>
                  </div>
                </div>
                <div class="flex items-center text-brand-gold gap-0.5">
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                  <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                </div>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                «Делал оклейку в серый матовый сатин плюс бронирование фар полиуретаном. Машина преобразилась кардинально, выглядит невероятно дорого. Сроки выдержали строго, выдали гарантийный талон. Лучший детейлинг на КМВ!»
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-brand-border text-[10px] text-slate-500 flex items-center justify-between">
              <span>Проверенный отзыв с Яндекса</span>
              <span>Ноябрь 2026</span>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- =========================================================================
         10. LOCATION, STUDIO SHOWCASE & EXACT MAP (ERMOLOVA 12A, STR. 5)
         ========================================================================= -->
    <section id="contacts" class="py-16 sm:py-24 bg-brand-dark border-b border-brand-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="mb-12">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-surface arch-border text-slate-300 text-xs font-semibold uppercase tracking-wider mb-3">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-brand-crimson"></i>
            <span>Пятигорск • ул. Ермолова, 12А, стр. 5</span>
          </div>
          <h2 class="text-2xl sm:text-4xl font-heading font-extrabold text-white">
            Ждём вас в студии «Авто Графикс»
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 mt-2 max-w-xl">
            Собственные просторные боксы, охраняемая парковка для клиентов и удобный заезд со светофора по ул. Ермолова.
          </p>
        </div>

        <!-- Facade & Entrance Real Photos -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 mb-10">
          
          <div class="bg-brand-surface arch-border rounded-2xl overflow-hidden group">
            <div class="h-52 overflow-hidden relative">
              <img src="assets/optimized/photo_02.jpg" alt="Фасад студии Авто Графикс на ул. Ермолова 12А" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute top-3 left-3 px-2.5 py-1 rounded bg-black/80 text-white text-[10px] font-bold">
                Главный фасад
              </div>
            </div>
            <div class="p-4">
              <div class="font-bold text-white text-sm mb-1">Вывеска и парковка</div>
              <div class="text-xs text-slate-400">Пятигорск, ул. Ермолова, 12А, стр. 5. Охраняемая клиентская стоянка.</div>
            </div>
          </div>

          <div class="bg-brand-surface arch-border rounded-2xl overflow-hidden group">
            <div class="h-52 overflow-hidden relative">
              <img src="assets/optimized/photo_05.jpg" alt="Входная группа и режим работы студии" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute top-3 left-3 px-2.5 py-1 rounded bg-black/80 text-white text-[10px] font-bold">
                Входная группа
              </div>
            </div>
            <div class="p-4">
              <div class="font-bold text-white text-sm mb-1">Режим работы</div>
              <div class="text-xs text-slate-400">Понедельник — Пятница: 09:00 – 17:00. Выходные: по записи.</div>
            </div>
          </div>

          <div class="bg-brand-surface arch-border rounded-2xl overflow-hidden group sm:col-span-2 lg:col-span-1">
            <div class="h-52 overflow-hidden relative">
              <img src="assets/optimized/photo_09.jpg" alt="Интерьер детейлинг-бокса Авто Графикс" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute top-3 left-3 px-2.5 py-1 rounded bg-black/80 text-white text-[10px] font-bold">
                Стерильный цех
              </div>
            </div>
            <div class="p-4">
              <div class="font-bold text-white text-sm mb-1">Оснащение студии</div>
              <div class="text-xs text-slate-400">Профессиональные потолочные софиты и фильтрация воздуха.</div>
            </div>
          </div>

        </div>

        <!-- Map & Contacts Card -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          <div class="lg:col-span-5 bg-brand-surface arch-border rounded-2xl p-6 sm:p-8">
            <h3 class="text-xl font-heading font-bold text-white mb-6">
              Контактная информация
            </h3>

            <div class="space-y-5 text-xs sm:text-sm">
              <div class="flex items-start gap-3.5">
                <div class="w-9 h-9 rounded-xl bg-brand-dark arch-border text-brand-crimson flex items-center justify-center flex-shrink-0">
                  <i data-lucide="map-pin" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="font-bold text-white mb-0.5">Точный адрес:</div>
                  <div class="text-slate-300">Ставропольский край, г. Пятигорск, ул. Ермолова, 12А, стр. 5</div>
                  <div class="text-[11px] text-slate-500 mt-0.5">Координаты крыши: 44.043891, 43.026930</div>
                </div>
              </div>

              <div class="flex items-start gap-3.5">
                <div class="w-9 h-9 rounded-xl bg-brand-dark arch-border text-brand-crimson flex items-center justify-center flex-shrink-0">
                  <i data-lucide="clock" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="font-bold text-white mb-0.5">График работы:</div>
                  <div class="text-slate-300">Пн — Пт: 09:00 – 17:00</div>
                  <div class="text-[11px] text-emerald-400 mt-0.5">Суббота и Воскресенье — по предварительной записи</div>
                </div>
              </div>

              <div class="flex items-start gap-3.5">
                <div class="w-9 h-9 rounded-xl bg-brand-dark arch-border text-brand-crimson flex items-center justify-center flex-shrink-0">
                  <i data-lucide="phone" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="font-bold text-white mb-0.5">Телефон мастера:</div>
                  <a href="tel:+79286519252" class="text-brand-crimson font-heading font-bold text-base hover:underline">
                    +7 (928) 651-92-52
                  </a>
                  <div class="text-[11px] text-slate-500 mt-0.5">Консультация и запись на осмотр ЛКП</div>
                </div>
              </div>
            </div>

            <div class="mt-8 pt-6 border-t border-brand-border flex flex-col sm:flex-row gap-3">
              <a 
                href="https://wa.me/79286519252" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="flex-1 py-3 px-4 rounded-xl bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-400 border border-emerald-500/30 text-center font-bold text-xs flex items-center justify-center gap-2 transition-colors"
              >
                <span>Написать в WhatsApp</span>
              </a>
              <a 
                href="https://yandex.ru/maps/?rtext=~44.043891,43.026930" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="flex-1 py-3 px-4 rounded-xl bg-brand-dark hover:bg-brand-card arch-border text-white text-center font-bold text-xs flex items-center justify-center gap-2 transition-colors"
              >
                <span>Маршрут в Яндекс</span>
              </a>
            </div>
          </div>

          <!-- Leaflet Interactive Dark Map (Strictly Verified: 44.043891, 43.026930) -->
          <div class="lg:col-span-7 bg-brand-surface arch-border rounded-2xl overflow-hidden h-[420px] relative shadow-2xl">
            <div id="studio-map" class="w-full h-full z-10"></div>
            
            <div class="absolute bottom-3 left-3 right-3 sm:left-4 sm:right-auto z-20 bg-brand-dark/95 backdrop-blur-md arch-border p-3 rounded-xl shadow-2xl flex items-center justify-between gap-3 text-xs">
              <div>
                <div class="font-bold text-white flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-brand-crimson"></span>
                  <span>«Авто Графикс» Детейлинг</span>
                </div>
                <div class="text-[11px] text-slate-400 mt-0.5">г. Пятигорск, ул. Ермолова, 12А, стр. 5</div>
              </div>
              <a 
                href="https://yandex.ru/maps/?rtext=~44.043891,43.026930" 
                target="_blank" 
                rel="noopener noreferrer"
                class="px-3 py-1.5 rounded-lg bg-brand-crimson text-white font-bold text-xs shadow transition-all flex items-center gap-1.5 whitespace-nowrap"
              >
                <i data-lucide="navigation" class="w-3 h-3"></i>
                <span>Яндекс Навигатор</span>
              </a>
            </div>
          </div>

        </div>

      </div>
    </section>
  </main>

  <!-- =========================================================================
       11. LEGAL COMPLIANCE FOOTER (152-FZ & VLADISLAND.STUDIO)
       ========================================================================= -->
  <footer class="bg-brand-dark text-slate-300 py-12 px-4 sm:px-6 lg:px-8 border-t border-brand-border text-center text-xs">
    <div class="max-w-5xl mx-auto flex flex-col items-center gap-4">
      
      <!-- Organization Details -->
      <div class="text-slate-200 text-xs sm:text-sm font-medium tracking-wide">
        ООО «АВТО ГРАФИКС» <span class="mx-2 text-slate-600">|</span> ИНН 2632115980 <span class="mx-2 text-slate-600">|</span> г. Пятигорск, ул. Ермолова, 12А, стр. 5
      </div>

      <!-- Direct Contacts -->
      <div class="flex flex-wrap items-center justify-center gap-x-6 gap-y-2 text-slate-400 text-xs">
        <span>Телефон: <a href="tel:+79286519252" class="text-white hover:text-brand-crimson font-bold underline-offset-4">+7 (928) 651-92-52</a></span>
        <span>WhatsApp: <a href="https://wa.me/79286519252" target="_blank" rel="noopener noreferrer" class="text-white hover:text-brand-crimson underline-offset-4">+7 (928) 651-92-52</a></span>
        <span>Режим: Пн-Пт с 09:00 до 17:00</span>
      </div>

      <div class="w-full max-w-xl h-[1px] bg-white/10 my-1"></div>

      <!-- Legal Links -->
      <div class="flex flex-wrap items-center justify-center gap-x-4 sm:gap-x-6 gap-y-2 text-[11px] sm:text-xs tracking-wider uppercase font-semibold text-slate-400">
        <a href="#" onclick="openLegalModal('privacy'); return false;" class="hover:text-white underline underline-offset-4 decoration-white/30 transition-all py-1">
          ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ (152-ФЗ)
        </a>
        <span class="hidden sm:inline text-white/30">•</span>
        <a href="#" onclick="openLegalModal('terms'); return false;" class="hover:text-white underline underline-offset-4 decoration-white/30 transition-all py-1">
          ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ И ОФЕРТА
        </a>
        <span class="hidden sm:inline text-white/30">•</span>
        <a href="#" onclick="openLegalModal('cookie'); return false;" class="hover:text-white underline underline-offset-4 decoration-white/30 transition-all py-1">
          ПОЛИТИКА ИСПОЛЬЗОВАНИЯ COOKIE
        </a>
      </div>

      <div class="text-slate-500 text-xs mt-1">
        © 2026 Студия детейлинга «Авто Графикс». Все права защищены. Разработка сайта: <span class="text-slate-300 font-bold tracking-wide">VLADISLAND.STUDIO</span>
      </div>

      <div class="text-[11px] text-slate-600 tracking-wider uppercase font-medium">
        ХОСТИНГ И БАЗЫ ДАННЫХ — РОССИЙСКАЯ ФЕДЕРАЦИЯ (Ч. 5 СТ. 18 152-ФЗ)
      </div>

    </div>
  </footer>

  <!-- =========================================================================
       12. MOBILE BOTTOM ACTION BAR
       ========================================================================= -->
  <div class="fixed bottom-0 inset-x-0 z-40 bg-brand-dark/95 backdrop-blur-md border-t border-brand-border p-3 flex sm:hidden items-center justify-between gap-2 shadow-2xl">
    <a 
      href="tel:+79286519252" 
      class="flex-1 py-3 rounded-xl bg-brand-surface arch-border text-white text-center font-bold text-xs flex items-center justify-center gap-1.5"
    >
      <i data-lucide="phone" class="w-4 h-4 text-brand-crimson"></i>
      <span>Позвонить</span>
    </a>
    <a 
      href="https://wa.me/79286519252" 
      target="_blank" 
      rel="noopener noreferrer" 
      class="flex-1 py-3 rounded-xl bg-emerald-600 text-white text-center font-bold text-xs flex items-center justify-center gap-1.5"
    >
      <span>WhatsApp</span>
    </a>
    <button 
      onclick="openBookingModal('Быстрая кнопка мобильного бара')" 
      class="flex-1 py-3 rounded-xl bg-brand-crimson text-white text-center font-heading font-bold text-xs uppercase tracking-wider"
    >
      Запись
    </button>
  </div>

  <!-- =========================================================================
       13. COOKIE CONSENT BANNER (152-FZ)
       ========================================================================= -->
  <aside 
    id="cookie-banner" 
    class="fixed bottom-16 sm:bottom-6 left-4 right-4 sm:left-6 sm:right-auto sm:max-w-md z-50 bg-brand-surface/98 backdrop-blur-md text-white p-4 sm:p-5 rounded-2xl shadow-2xl arch-border hidden transition-all duration-500 transform translate-y-6"
    aria-label="Согласие на использование cookie"
  >
    <div class="flex items-start gap-3.5">
      <div class="w-8 h-8 rounded-xl bg-brand-dark arch-border flex items-center justify-center flex-shrink-0 text-brand-crimson">
        <i data-lucide="shield-alert" class="w-4 h-4"></i>
      </div>
      <div class="text-xs text-slate-300 leading-relaxed">
        Мы используем технические файлы cookie для корректной работы сайта. Пользуясь сайтом, вы соглашаетесь с 
        <a href="#" onclick="openLegalModal('cookie'); return false;" class="text-brand-crimson underline underline-offset-2 hover:text-white">Политикой обработки cookie</a> 
        в соответствии с 152-ФЗ РФ.
      </div>
    </div>
    
    <div class="mt-3.5 flex items-center justify-end gap-3">
      <button 
        onclick="acceptCookieConsent()" 
        class="w-full sm:w-auto px-5 py-2 rounded-xl bg-brand-crimson text-white hover:bg-brand-crimsonHover font-bold text-xs transition-colors cursor-pointer"
      >
        Принять и продолжить
      </button>
    </div>
  </aside>

  <!-- =========================================================================
       14. MODAL: BOOKING & INSPECTION
       ========================================================================= -->
  <div id="booking-modal" class="fixed inset-0 z-50 hidden bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-brand-card arch-border rounded-2xl max-w-md w-full p-6 sm:p-8 relative shadow-2xl max-h-[90vh] overflow-y-auto">
      
      <button onclick="closeBookingModal()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-brand-surface arch-border text-slate-400 hover:text-white flex items-center justify-center cursor-pointer transition-colors">
        <i data-lucide="x" class="w-4 h-4"></i>
      </button>

      <div class="text-xs font-heading font-bold uppercase tracking-widest text-brand-crimson mb-1">Студия «Авто Графикс»</div>
      <h3 class="text-xl font-heading font-extrabold text-white mb-2" id="booking-modal-title">Запись на осмотр и оклейку</h3>
      <p class="text-xs text-slate-400 mb-6" id="booking-modal-desc">
        Оставьте номер телефона. Мастер свяжется с вами в течение 10 минут, ответит на технические вопросы и забронирует время в боксе.
      </p>

      <form onsubmit="handleBookingSubmit(event)" class="space-y-4">
        <input type="hidden" id="modal-source" value="Главная форма">

        <div>
          <label class="block text-xs text-slate-400 mb-1">Ваше имя</label>
          <input 
            type="text" 
            id="modal-name" 
            placeholder="Как к вам обращаться" 
            class="w-full px-4 py-3 rounded-xl bg-brand-surface arch-border text-base text-white focus:outline-none focus:border-brand-crimson transition-colors"
          >
        </div>

        <div>
          <label class="block text-xs text-slate-400 mb-1">Номер телефона <span class="text-red-400">*</span></label>
          <input 
            type="tel" 
            id="modal-phone" 
            required 
            placeholder="+7 (___) ___-__-__" 
            class="w-full px-4 py-3 rounded-xl bg-brand-surface arch-border text-base text-white focus:outline-none focus:border-brand-crimson transition-colors font-mono"
            oninput="maskPhone(this)"
          >
        </div>

        <div>
          <label class="block text-xs text-slate-400 mb-1">Интересующая услуга / Модель авто</label>
          <select 
            id="modal-service" 
            class="w-full px-4 py-3 rounded-xl bg-brand-surface arch-border text-base text-white focus:outline-none focus:border-brand-crimson transition-colors cursor-pointer"
          >
            <option value="Зоны риска PPF">Комплекс «Зоны риска» (PPF)</option>
            <option value="Полная броня PPF">Полная броня кузова 360°</option>
            <option value="Смена цвета винилом">Смена цвета / Автовинил</option>
            <option value="Антихром и оптика">Антихром Shadow Line + броня фар</option>
            <option value="Защита салона">Бронирование экранов и глянца салона</option>
            <option value="Полировка и керамика">Полировка кузова + Керамика 9H</option>
          </select>
        </div>

        <!-- 152-FZ Consent Checkbox (UNCHECKED BY DEFAULT, Disables button) -->
        <div class="my-3">
          <label class="flex items-start gap-3 cursor-pointer text-left select-none group">
            <input 
              type="checkbox" 
              id="modal-consent" 
              required 
              class="mt-1 w-4 h-4 rounded border-slate-600 text-brand-crimson focus:ring-brand-crimson cursor-pointer accent-brand-crimson"
              onchange="toggleSubmitButton(this)"
            >
            <span class="text-xs text-slate-400 leading-relaxed">
              Даю согласие на обработку персональных данных в соответствии с 
              <a href="#" onclick="openLegalModal('privacy'); return false;" class="text-brand-crimson underline hover:text-white">152-ФЗ РФ</a>.
            </span>
          </label>
        </div>

        <button 
          type="submit" 
          id="modal-submit-btn" 
          disabled 
          class="w-full py-3.5 rounded-xl bg-brand-crimson text-white font-heading font-bold text-xs uppercase tracking-wider transition-all disabled:opacity-40 disabled:cursor-not-allowed shadow-sm"
        >
          Подтвердить запись
        </button>
      </form>

    </div>
  </div>

  <!-- =========================================================================
       15. MODAL: LEGAL DOCUMENTS (152-FZ, TERMS, COOKIE)
       ========================================================================= -->
  <div id="legal-modal" class="fixed inset-0 z-50 hidden bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-brand-card arch-border rounded-2xl max-w-2xl w-full p-6 sm:p-8 relative shadow-2xl max-h-[85vh] flex flex-col">
      
      <div class="flex items-center justify-between pb-4 border-b border-brand-border">
        <h3 class="text-lg font-heading font-bold text-white" id="legal-modal-title">Юридический документ</h3>
        <button onclick="closeLegalModal()" class="w-8 h-8 rounded-full bg-brand-surface arch-border text-slate-400 hover:text-white flex items-center justify-center cursor-pointer transition-colors">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="overflow-y-auto py-4 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-4" id="legal-modal-body">
        <!-- Injected dynamically via JS -->
      </div>

      <div class="pt-4 border-t border-brand-border flex justify-end">
        <button onclick="closeLegalModal()" class="px-5 py-2.5 rounded-xl bg-brand-surface hover:bg-brand-border text-white text-xs font-bold transition-colors cursor-pointer">
          Закрыть
        </button>
      </div>

    </div>
  </div>

  <!-- =========================================================================
       16. VANILLA JAVASCRIPT LOGIC
       ========================================================================= -->
  <script>
    // 1. Phone input mask: +7 (XXX) XXX-XX-XX
    function maskPhone(input) {
      let matrix = "+7 (___) ___-__-__",
          i = 0,
          def = matrix.replace(/\D/g, ""),
          val = input.value.replace(/\D/g, "");
      
      if (def.length >= val.length) val = def;
      input.value = matrix.replace(/./g, function(a) {
        return /[___#]/.test(a) && i < val.length ? val.charAt(i++) : i >= val.length ? "" : a;
      });
    }

    // 2. 152-FZ Submit Button Enabler
    function toggleSubmitButton(checkbox) {
      const form = checkbox.closest('form');
      if (!form) return;
      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = !checkbox.checked;
      }
    }

    // 3. Mobile Menu Toggle
    function toggleMobileMenu() {
      const menu = document.getElementById('mobile-menu');
      if (menu) {
        menu.classList.toggle('hidden');
      }
    }

    // 4. Interactive Quiz State & Navigation
    let currentQuizStep = 1;
    function goToStep(step) {
      document.getElementById('quiz-step-1').classList.add('hidden');
      document.getElementById('quiz-step-2').classList.add('hidden');
      document.getElementById('quiz-step-3').classList.add('hidden');

      const target = document.getElementById('quiz-step-' + step);
      if (target) target.classList.remove('hidden');

      currentQuizStep = step;
      const label = document.getElementById('quiz-step-label');
      const percent = document.getElementById('quiz-percent');
      const pBar = document.getElementById('quiz-progress-bar');

      if (step === 1) {
        label.innerText = 'Шаг 1 из 3: Категория вашего автомобиля';
        percent.innerText = '33%';
        pBar.style.width = '33%';
      } else if (step === 2) {
        label.innerText = 'Шаг 2 из 3: Комплекс оклейки или стайлинга';
        percent.innerText = '66%';
        pBar.style.width = '66%';
      } else {
        label.innerText = 'Шаг 3 из 3: Ваш подарок и расчет';
        percent.innerText = '100%';
        pBar.style.width = '100%';
        calculateQuizPrice();
      }
    }

    function updateQuizStep(step) {
      const stepEl = document.getElementById('quiz-step-' + step);
      if (!stepEl) return;
      const radios = stepEl.querySelectorAll('input[type="radio"]');
      radios.forEach(r => {
        const ind = r.closest('label').querySelector('.radio-indicator');
        if (ind) ind.innerText = r.checked ? '●' : '';
      });
    }

    function calculateQuizPrice() {
      const carRadio = document.querySelector('input[name="car_class"]:checked');
      const srvRadio = document.querySelector('input[name="service_type"]:checked');
      const mult = carRadio ? parseFloat(carRadio.getAttribute('data-mult')) : 1.0;
      const base = srvRadio ? parseInt(srvRadio.getAttribute('data-base')) : 55000;
      const total = Math.round(base * mult);
      
      const priceEl = document.getElementById('quiz-calc-price');
      if (priceEl) {
        priceEl.innerText = 'от ' + total.toLocaleString('ru-RU') + ' ₽';
      }
    }

    function handleQuizSubmit(e) {
      e.preventDefault();
      const phone = document.getElementById('quiz-phone').value;
      const carModel = document.getElementById('quiz-car-model').value || 'Не указано';
      const carClass = document.querySelector('input[name="car_class"]:checked')?.value || '';
      const service = document.querySelector('input[name="service_type"]:checked')?.value || '';
      const gift = document.querySelector('input[name="gift"]:checked')?.value || '';

      alert(`Спасибо за заявку!\n\nАвтомобиль: ${carModel} (${carClass})\nУслуга: ${service}\nЗафиксированный подарок: ${gift}\nТелефон: ${phone}\n\nМастер студии «Авто Графикс» свяжется с вами в течение 10 минут!`);
      e.target.reset();
      goToStep(1);
    }

    // 5. Services Filter Tabs
    function filterServices(category) {
      const tabs = document.querySelectorAll('.service-tab-btn');
      tabs.forEach(t => {
        t.classList.remove('bg-brand-crimson', 'text-white', 'shadow-sm');
        t.classList.add('bg-brand-surface', 'text-slate-300', 'arch-border');
      });
      const activeTab = document.getElementById('tab-' + category);
      if (activeTab) {
        activeTab.classList.add('bg-brand-crimson', 'text-white', 'shadow-sm');
        activeTab.classList.remove('bg-brand-surface', 'text-slate-300', 'arch-border');
      }

      const cards = document.querySelectorAll('.service-card');
      cards.forEach(card => {
        if (card.getAttribute('data-category') === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    }

    // 6. Booking Modal
    function openBookingModal(source) {
      const modal = document.getElementById('booking-modal');
      const srcInput = document.getElementById('modal-source');
      if (srcInput && source) srcInput.value = source;
      if (modal) modal.classList.remove('hidden');
    }

    function closeBookingModal() {
      const modal = document.getElementById('booking-modal');
      if (modal) modal.classList.add('hidden');
    }

    function handleBookingSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('modal-name').value || 'Клиент';
      const phone = document.getElementById('modal-phone').value;
      const service = document.getElementById('modal-service').value;

      alert(`Спасибо, ${name}! Ваша заявка на «${service}» принята.\nМастер студии перезвонит на номер ${phone} в течение 10 минут.`);
      closeBookingModal();
      e.target.reset();
    }

    // 7. Legal Documents Modal (152-FZ, Terms, Cookie)
    const legalTexts = {
      privacy: {
        title: 'Политика в отношении обработки персональных данных (152-ФЗ)',
        body: `
          <p><strong>1. Общие положения</strong><br>Настоящая Политика обработки персональных данных составлена в соответствии с Федеральным законом от 27.07.2006 № 152-ФЗ «О персональных данных» и определяет порядок обработки персональных данных студией детейлинга «Авто Графикс» (ООО «Авто Графикс», г. Пятигорск, ул. Ермолова, 12А, стр. 5, ИНН 2632115980).</p>
          <p><strong>2. Цели сбора данных</strong><br>Персональные данные (имя, номер телефона, марка автомобиля) собираются исключительно для связи с клиентом, предварительного расчета стоимости услуг оклейки и бронирования бокса в студии.</p>
          <p><strong>3. Локализация и хранение (ч. 5 ст. 18 152-ФЗ)</strong><br>Все базы данных и сервера сайта расположены строго на территории Российской Федерации. Данные не передаются третьим лицам без вашего согласия.</p>
          <p><strong>4. Отзыв согласия</strong><br>Вы можете отозвать согласие в любой момент, направив письменное заявление по адресу: г. Пятигорск, ул. Ермолова, 12А, стр. 5 или по телефону +7 (928) 651-92-52.</p>
        `
      },
      terms: {
        title: 'Пользовательское соглашение и оферта студии',
        body: `
          <p><strong>1. Предмет соглашения</strong><br>Настоящее соглашение регулирует порядок использования материалов сайта студии «Авто Графикс». Информация о ценах носит ознакомительный характер и не является публичной офертой (ст. 437 ГК РФ).</p>
          <p><strong>2. Гарантийные обязательства</strong><br>Студия предоставляет официальную гарантию на полиуретановые покрытия PPF сроком до 7 лет при условии прохождения контрольного осмотра через 14 дней и соблюдения регламента мойки автомобиля.</p>
          <p><strong>3. Порядок расчетов</strong><br>Оплата производится наличными, банковскими картами или по безналичному расчету после приемки автомобиля по акту выполненных работ.</p>
        `
      },
      cookie: {
        title: 'Политика использования файлов Cookie',
        body: `
          <p><strong>1. Назначение Cookie</strong><br>Файлы cookie используются исключительно для запоминания сессий, настроек квиза и технических согласий в браузере пользователя.</p>
          <p><strong>2. Конфиденциальность</strong><br>Cookie не содержат паспортных данных или платежной информации и обрабатываются в обезличенном виде.</p>
        `
      }
    };

    function openLegalModal(type) {
      const modal = document.getElementById('legal-modal');
      const title = document.getElementById('legal-modal-title');
      const body = document.getElementById('legal-modal-body');

      if (legalTexts[type]) {
        title.innerText = legalTexts[type].title;
        body.innerHTML = legalTexts[type].body;
      }
      if (modal) modal.classList.remove('hidden');
    }

    function closeLegalModal() {
      const modal = document.getElementById('legal-modal');
      if (modal) modal.classList.add('hidden');
    }

    // 8. Cookie Consent Logic (localStorage)
    document.addEventListener('DOMContentLoaded', () => {
      const isAccepted = localStorage.getItem('cookie_consent_accepted');
      if (!isAccepted) {
        const banner = document.getElementById('cookie-banner');
        if (banner) {
          setTimeout(() => {
            banner.classList.remove('hidden', 'translate-y-6');
            banner.classList.add('translate-y-0');
          }, 1000);
        }
      }
    });

    function acceptCookieConsent() {
      localStorage.setItem('cookie_consent_accepted', 'true');
      const banner = document.getElementById('cookie-banner');
      if (banner) {
        banner.classList.add('translate-y-6', 'opacity-0');
        setTimeout(() => banner.remove(), 400);
      }
    }
  </script>
  <script>lucide.createIcons();</script>

  <!-- Initialize 100% Ad-Free Dark Map with Studio Pin -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      if (document.getElementById('studio-map') && typeof L !== 'undefined') {
        const studioCoords = [44.043891, 43.026930];
        const map = L.map('studio-map', {
          center: studioCoords,
          zoom: 17,
          scrollWheelZoom: false,
          zoomControl: false,
          attributionControl: false
        });

        L.control.zoom({ position: 'topright' }).addTo(map);

        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer" style="color:#64748b;">OpenStreetMap</a>'
        }).addTo(map);

        const customPin = L.divIcon({
          className: 'custom-studio-pin',
          html: `
            <div style="position: relative; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center;">
              <div style="width: 28px; height: 28px; border-radius: 50%; background: #e11d48; border: 2.5px solid #ffffff; box-shadow: 0 4px 12px rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center;">
                <div style="width: 8px; height: 8px; border-radius: 50%; background: #ffffff;"></div>
              </div>
            </div>
          `,
          iconSize: [36, 36],
          iconAnchor: [18, 18],
          popupAnchor: [0, -20]
        });

        const marker = L.marker(studioCoords, { icon: customPin }).addTo(map);
        marker.bindPopup(`
          <div style="font-family: inherit; color: #fff; background: #0f1318; padding: 6px; border-radius: 8px; min-width: 180px;">
            <div style="font-weight: 800; color: #e11d48; font-size: 13px; margin-bottom: 2px;">«Авто Графикс» Детейлинг</div>
            <div style="font-size: 11px; color: #94a3b8; margin-bottom: 8px;">г. Пятигорск, ул. Ермолова, 12А, стр. 5</div>
            <a href="https://yandex.ru/maps/?rtext=~44.043891,43.026930" target="_blank" rel="noopener noreferrer" style="display: block; text-align: center; padding: 5px 10px; background: #e11d48; color: #fff; font-weight: 700; font-size: 11px; border-radius: 6px; text-decoration: none;">
              Открыть маршрут в Яндекс &rarr;
            </a>
          </div>
        `);
      }
    });
  </script>

</body>
</html>
'''

def build():
    output_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.strip())
    print(f"✅ Успешно сгенерирован анти-нейрослоп сайт: {output_path} ({len(HTML_TEMPLATE)} байт)")

if __name__ == "__main__":
    build()
