from __future__ import annotations

import html
import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve()
IN_REPOSITORY = HERE.parent.name == "scripts"
OUT = HERE.parents[1] if IN_REPOSITORY else Path("work/site_patch")
BASE = "https://romariobro.github.io/projectportfolio"


def rec(id, slug, title, source, date, url, kind, group, topics, project, about, role,
        facts, image, status="verified", published=True, featured=False, note=""):
    return locals()


R = [
rec("A01","interactive-advertising-rb","Интерактивная реклама: как продвигаются BBC, Mercedes-Benz и Discovery","RB.RU","2015-10-14","https://rb.ru/columns/new-ads/","BY_ME","By Me",["Marketing","Digital Transformation"],"ThingLink Russia","Author / Director of Business Development, ThingLink Russia","Author / Director of Business Development, ThingLink Russia",["Interactive advertising formats","Digital engagement","International brand examples"],"projects-media/seo-growth-300.webp",featured=False,note="Title, date, authorship and role verified on the original RB.RU page."),
rec("A02","project-management-it-gamedev-part-1","Как я управлял проектами в IT и GameDev, и что из этого понял — Часть 1","Habr","2025-06-13","https://habr.com/ru/articles/918184/","BY_ME","By Me",["Project Management","Product","GameDev"],"Professional Practice","A practical essay on teams, uncertainty, MVPs and delivery across IT and game development.","Author — Roman Mironichev / RomarioHabr",["Practical project-management observations","Cross-functional delivery","MVP and product development"],"projects-media/delivery-dashboard.webp",featured=False,note="Title, date and author verified on Habr."),
rec("A03","project-management-system-part-2","Часть 2. Почему система управления в проекте — это не просто «доска задач». От проблем к решениям","Habr","2025-06-15","https://habr.com/ru/articles/918594/","BY_ME","By Me",["Project Management","Product Operations"],"Professional Practice","A practical article on project-system design, delivery obstacles and moving from fragmented tasks to managed execution.","Author — Roman Mironichev / RomarioHabr",["Project operating system","Delivery visibility","Problem resolution"],"projects-media/delivery-dashboard.webp",featured=True,note="Title, date and author verified on Habr."),
rec("A04","ai-in-project-management","Про зарплаты проджектов ИТ, человеческое отношение к сотрудникам и ИИ в проектном менеджменте — Часть 3","Habr","2025-06-15","https://habr.com/ru/articles/918596/","BY_ME","By Me",["AI","Project Management"],"Professional Practice","An authored article on project-management compensation, humane team leadership and AI-assisted project work.","Author — Roman Mironichev / RomarioHabr",["AI in project management","Human-centered leadership","Delivery under change"],"projects-media/delivery-dashboard.webp",featured=True,note="Title, date and author verified on Habr."),
rec("A05","gamedev-vs-it-linkedin","GameDev vs IT","LinkedIn","2024-08-16","https://www.linkedin.com/in/roman-mironichev-69b63614/","BY_ME","By Me",["GameDev","Product"],"Professional Practice","LinkedIn publication record without a stable post URL.","Author",[],"projects-media/game-simulator.webp","needs_recheck",False,note="Profile-only URL; exact post permalink is required."),
rec("A06","youtube-summarizer-linkedin","YouTube Summarizer","LinkedIn","2026-03-24","https://www.linkedin.com/in/roman-mironichev-69b63614/","BY_ME","By Me",["AI","Product"],"AI Product","LinkedIn publication record without a stable post URL.","Author",[],"projects-media/delivery-dashboard.webp","needs_recheck",False,note="Profile-only URL; exact post permalink is required."),
rec("P02","pr-club-spb-publication","Personal publication in PR Club SPb","PR Club SPb","2015-12-10","","BY_ME","By Me",["Marketing","PR"],"Professional Practice","Publication record awaiting a stable original article URL.","Author",[],"projects-media/seo-growth-300.webp","needs_recheck",False,note="A profile reference exists, but the exact original publication URL is unresolved."),
rec("P08","emotions-with-a-head-dp","Во сколько работодателям обходится игнорирование эмоциональной подавленности работников","Деловой Петербург","2017-03-08","https://www.dp.ru/a/2017/03/06/JEmocii_s_golovoj","PERSONAL_MENTION","Personal Mentions",["Management","Operations"],"Exiclub","External article quoting Roman Mironichev on employee emotional state, productivity and business impact.","Expert Commentator / CEO, Exiclub",["Independent media mention","Expert commentary","Employee productivity"],"projects-media/seo-growth-300.webp",featured=True,note="Title, publication date, quote and CEO attribution verified on DP.ru."),
rec("P09","talk-for-dev-cms-magazine","ПОговорим за виртуалку?","CMS Magazine","2016-10-20","https://cmsmagazine.ru/journal/items-talk-for-dev/","PERSONAL_MENTION","Personal Mentions",["Project Management","Digital Transformation"],"Privetmarketing","Industry round-up featuring Roman Mironichev on collaboration tools, remote work and project communications.","Expert Contributor / Founder, Privetmarketing",["Independent media mention","Remote collaboration","Digital project tools"],"projects-media/delivery-dashboard.webp",featured=False,note="Title, date, name and founder attribution verified on CMS Magazine."),

rec("B01","simdaq-raised-5m","SIMDAQ raises $5 million in Waves Lab incubation","CryptoNinjas","2018-01-29","https://www.cryptoninjas.net/2018/01/29/first-waves-lab-ico-incubation-simdaq-raises-5-million/","PROJECT_IN_MEDIA","Projects in the Media",["FinTech","Product","Blockchain"],"SIMDAQ","Independent coverage of SIMDAQ funding and the Waves Lab incubation program.","Product Management / Growth Operations contributor; coordinated MVP, roadmap, gamification and international launch.",["$5M raised","15+ specialists","30+ product screens"],"projects-media/simdaq-dashboard.webp",featured=True),
rec("B02","simdaq-waves-lab","SIMDAQ joins the Waves Lab blockchain incubator","CryptoNinjas","2018-01-22","https://www.cryptoninjas.net/2018/01/22/first-projects-get-started-new-waves-lab-blockchain-incubator/","PROJECT_IN_MEDIA","Projects in the Media",["FinTech","Blockchain"],"SIMDAQ","Independent coverage of the first projects entering Waves Lab.","Product Management / Growth Operations contributor.",["International FinTech startup","Incubation and product launch context"],"projects-media/simdaq-simulation.webp"),
rec("B03","simdaq-trading-marketplace","SIMDAQ to launch a crypto trading strategy marketplace","CryptoNinjas","2017-11-20","https://www.cryptoninjas.net/2017/11/20/simdaq-launch-ico-crypto-trading-strategy-marketplace/","PROJECT_IN_MEDIA","Projects in the Media",["FinTech","Product","Blockchain"],"SIMDAQ","Product coverage describing the historical-data trading simulator and strategy marketplace concept.","Contributed to MVP, Customer Development, roadmap and gamification.",["Historical financial data","Trading simulator","Marketplace concept"],"projects-media/simdaq-statistics.webp"),
rec("B04","simdaq-marketplace-waves","SIMDAQ marketplace based on Waves smart contracts","SIMDAQ on Medium","2018-05-23","https://medium.com/simdaq-blog/simdaq-launching-the-marketplace-for-traders-based-on-waves-smart-contracts-1711e0b240f5","PRODUCT_REFERENCE","References",["FinTech","Product","Blockchain"],"SIMDAQ","Official project publication explaining marketplace mechanics and the first release.","Product Management / Growth Operations contributor; this is a project publication, not personal authorship.",["$5M token sale stated by source","Simulation and analytics","Training content"],"projects-media/simdaq-dashboard.webp",featured=True),
rec("B05","simdaq-development-may-2018","SIMDAQ project development report — May 2018","SIMDAQ on Medium","2018-05-10","https://medium.com/simdaq-blog/simdaq-project-development-report-may-2018-9a0feba2daf6","PRODUCT_REFERENCE","References",["FinTech","Product"],"SIMDAQ","Official project development update.","Project contributor; not personal authorship.",[],"projects-media/simdaq-simulation.webp","needs_recheck",False,note="Medium blocks automated access; exact page not independently indexed in this audit."),
rec("B06","simdaq-development-nov-2018","SIMDAQ project development report — November 2018","SIMDAQ on Medium","2018-11-13","https://medium.com/simdaq-blog/simdaq-project-development-report-8d6b19ab0102","PRODUCT_REFERENCE","References",["FinTech","Product"],"SIMDAQ","Official post-launch development update.","Project contributor; not personal authorship.",[],"projects-media/simdaq-statistics.webp","needs_recheck",False,note="Medium blocks automated access; exact page not independently indexed in this audit."),
rec("B07","simdaq-reward-program","SIMDAQ reward and contest program","SIMDAQ on Medium","2018-07-27","https://medium.com/simdaq-blog/simdaq-reward-and-contest-program-stage-i-10c27eec028f","PRODUCT_REFERENCE","References",["FinTech","Growth"],"SIMDAQ","Official project publication on reward and contest mechanics.","Project contributor; not personal authorship.",[],"projects-media/simdaq-dashboard.webp","needs_recheck",False,note="Medium blocks automated access; exact page not independently indexed in this audit."),

rec("C01","gamblica-coinspeaker","Gamblica and blockchain-integrated gaming","Coinspeaker","2018-04-23","https://www.coinspeaker.com/startup-gamblica-wants-turn-gambling-industry-upside-blockchain-tech/","PROJECT_IN_MEDIA","Projects in the Media",["Product","Blockchain","GameDev"],"Digital Finance Project / Gamblica","Independent media coverage of the international digital product concept and launch.","Product + PMO + Operations: roadmap, MVP, launch and cross-functional growth operations.",["$1.7M first investment round","$3M+ total funding","International launch"],"projects-media/game-simulator.webp",featured=True),
rec("C02","gamblica-newsbtc-sponsored","Gamblica: blockchain-integrated online product","NewsBTC","2018","https://www.newsbtc.com/sponsored/gamblica-a-new-addition-in-blockchain-integrated-online-gambling-industry/","PROJECT_IN_MEDIA","Projects in the Media",["Product","Blockchain","Growth"],"Digital Finance Project / Gamblica","Sponsored product coverage. Presented as project media, not independent editorial endorsement.","Product + PMO + Operations contributor.",["Acquisition, engagement, monetization and retention","International product development"],"projects-media/game-simulator.webp"),
rec("C03","gamblica-newsbtc-release","Gamblica platform token-sale coverage","NewsBTC","2018","https://www.newsbtc.com/press-releases/gamblica-innovative-blockchain-gambling-platform/","PROJECT_IN_MEDIA","Projects in the Media",["Product","Blockchain","PR"],"Digital Finance Project / Gamblica","Press-release coverage of the product and funding campaign.","Product + PMO + Operations contributor; not the article author.",["Product strategy","MVP","International Go-to-Market"],"projects-media/game-simulator.webp"),
rec("C04","gamblica-coinspeaker-profile","Gamblica ICO project profile","Coinspeaker","2018","https://www.coinspeaker.com/ico/gamblica/","PRODUCT_REFERENCE","References",["Product","Blockchain"],"Digital Finance Project / Gamblica","Directory profile retained as a product reference.","Product + PMO + Operations contributor.",["Project profile","Funding and launch context"],"projects-media/game-simulator.webp"),
rec("C05","gamblica-medium-update","Gamblica project update","Gamblica on Medium","2018-12-06","https://medium.com/@gamblica/99-6-cc95f1b68685","PRODUCT_REFERENCE","References",["Product","Blockchain"],"Digital Finance Project / Gamblica","Official project update.","Project contributor; not personal authorship.",[],"projects-media/game-simulator.webp","needs_recheck",False,note="Medium blocks automated access; exact page requires a manual recheck."),
rec("C06","gamblica-icomarks","Gamblica project archive","ICOmarks","2018","https://icomarks.ai/ico/gamblica","MEDIA_ARCHIVE","References",["Product","Blockchain"],"Digital Finance Project / Gamblica","Third-party directory archive retained for historical reference.","Project + operations contributor; directory attribution only.",["Historical archive"],"projects-media/game-simulator.webp","reference_only",True),

rec("D01","samolet-online-apartment-vcru","How buying an apartment became an end-to-end online journey","vc.ru / Samolet","2020","https://vc.ru/samolet/206364-kak-kupit-kvartiru-stalo-proshe-chem-shodit-v-magazin","PROJECT_IN_MEDIA","Projects in the Media",["Digital Transformation","Marketing","Product","Real Estate"],"SAMOLET Digital Transformation","Company publication on the remote apartment-purchase journey accelerated during COVID-19.","Digital Transformation Project Lead connecting web, mobile, CRM, analytics and customer journey initiatives to business cases and P&L.",["10 departments","RUB 950M economic impact in 2019","RUB 1.5B projected portfolio impact in 2020"],"projects-media/seo-growth-300.webp",featured=True),
rec("D02","samolet-bankinform","SAMOLET remote real-estate transactions","Bankinform","2020-04-17","https://bankinform.ru/news/104730","PROJECT_IN_MEDIA","Projects in the Media",["Digital Transformation","Real Estate"],"SAMOLET Digital Transformation","External publication on remote real-estate transactions.","Digital Transformation Project Lead.",[],"projects-media/seo-growth-300.webp","needs_recheck",False,note="SSL validation failed during automated audit; manual browser recheck required."),
rec("D03","samolet-online-mortgage","Rosbank and SAMOLET complete online mortgage transactions","Global CIO","2020","https://globalcio.ru/news/6084/","PROJECT_IN_MEDIA","Projects in the Media",["Digital Transformation","FinTech","Real Estate"],"SAMOLET Digital Transformation","Independent coverage of online mortgage transactions.","Led digital transformation initiatives across marketing and commercial functions.",["Web, mobile and CRM","Customer journey","Investment governance"],"projects-media/seo-growth-300.webp"),
rec("D04","samolet-cian-online","How to buy an apartment without leaving home","CIAN","2020-04-29","https://www.cian.ru/stati-kak-kupit-kvartiru-ne-vyhodja-iz-doma-305128/","PROJECT_IN_MEDIA","Projects in the Media",["Digital Transformation","Real Estate","Marketing"],"SAMOLET Digital Transformation","External coverage of the end-to-end remote apartment journey.","Digital Transformation Project Lead; no claim that SAMOLET invented all online sales.",["COVID-19 accelerated remote transactions","Customer journey transformation"],"projects-media/seo-growth-300.webp"),
rec("D05","samolet-vedomosti-digital","Buying an apartment over a cup of coffee","Vedomosti","2020-12-02","https://www.vedomosti.ru/partner/articles/2020/12/02/849060-kupit-kvartiru","PROJECT_IN_MEDIA","Projects in the Media",["Digital Transformation","Marketing","Real Estate"],"SAMOLET Digital Transformation","Partner material describing a simplified digital home-buying journey.","Led transformation portfolio governance and measurable marketing/commercial improvements.",["+9% advertising traffic efficiency","−15% advertising cost per transaction","2–10% department efficiency"],"projects-media/seo-growth-300.webp",featured=True),

rec("E01","rr-transport-processing-ifellow","Raschetnye Resheniya, Strelka and transport processing","iFellow","","https://ifellow.ru/media-center/raschetnye-resheniya-dochka-sbera-karta-strelka-i-razvitie-transportnogo-protsessinga/","COMPANY_REFERENCE","References",["FinTech","Product"],"SBER / AO RASCHETNYE RESHENIYA","Company and industry context for transport payment processing infrastructure.","Project Lead — Transportation Payment Processing.",["100M+ transactions/day","40 regions","40+ core development team"],"projects-media/transport-payments.webp",featured=True),
rec("E02","transport-bank-card-pass","Bank card as a unified transport pass","Argumenty i Fakty","","https://aif.ru/society/ptransport/platim_po-novomu_v_transporte_bankovskaya_karta_edinyy_proezdnoy","PROJECT_IN_MEDIA","Projects in the Media",["FinTech","Product"],"Transportation Payment Processing","Independent media context for cashless transport payments.","Led prioritization, roadmap, development, testing, releases, production and scaling.",["14 major production releases","8 product features"],"projects-media/transport-payments.webp"),
rec("E03","rr-cnews-archive","Raschetnye Resheniya CNews archive","CNews","","","MEDIA_ARCHIVE","References",["FinTech"],"SBER / AO RASCHETNYE RESHENIYA","Discovery-only archive record.","No publication claim.",[],"projects-media/transport-payments.webp","needs_recheck",False,note="Registry URL pattern is malformed; no stable article URL confirmed."),
rec("E04","rr-official","AO Raschetnye Resheniya — official company site","AO Raschetnye Resheniya","","https://www.ao-rr.ru/","COMPANY_REFERENCE","References",["FinTech","Product"],"SBER / AO RASCHETNYE RESHENIYA","Official source for the company and its payment infrastructure products.","Project Lead — Transportation Payment Processing.",["Cashless payment infrastructure","Transport systems","Digital public-service solutions"],"projects-media/transport-payments.webp"),

rec("F01","aether-games-interview","Aether Games interview: product vision and AR","Games.gg","","https://games.gg/news/exclusive-interview-with-aether-games/","PROJECT_IN_MEDIA","Projects in the Media",["Product","GameDev"],"REDRIFT / Aether Games","Independent interview about a portfolio product and its market positioning.","Head of PMO / Product Delivery across a 150+ international product organization.",["10+ products and initiatives","10+ Project/Product Managers","150+ specialists"],"projects-media/game-simulator.webp"),
rec("F02","cards-of-ethernity-razer","Cards of Ethernity product listing","Razer Game Deals","","https://deals.razer.com/games/cards-of-ethernity","PRODUCT_REFERENCE","References",["Product","GameDev"],"REDRIFT / Cards of Ethernity","Third-party product listing retained as evidence of an international portfolio release.","Portfolio Operations / Product Delivery leadership; no authorship claim.",["Idea → MVP → launch → growth → LiveOps"],"projects-media/game-simulator.webp"),
rec("F03","storyspark-redrift","How Red Rift changed the interactive stories market","Red Rift on Medium","2023-08-04","https://medium.com/@redrift/how-red-rift-changed-the-interactive-stories-market-forever-33b7fbf843db","PRODUCT_REFERENCE","References",["Product","GameDev","Growth"],"REDRIFT / StorySpark","Official company publication describing the StorySpark product.","Head of PMO / Product Delivery; company publication, not personal authorship.",["Interactive storytelling","Product development","International launch"],"projects-media/game-simulator.webp"),
rec("F04","storyspark-app-store","StorySpark Interactive Story — App Store","Apple App Store","","https://apps.apple.com/ru/app/storyspark-interactive-story/id1665916639","PRODUCT_REFERENCE","References",["Product","GameDev"],"REDRIFT / StorySpark","App Store listing from the registry.","Portfolio Operations / Product Delivery.",[],"projects-media/game-simulator.webp","needs_recheck",False,note="Registry URL returned 404 on 2026-08-16."),
rec("F05","berserk-cataclysm","Berserk: The Cataclysm — product video","YouTube / Vulcan Forged","","https://www.youtube.com/watch?v=jeGgC-FibIA","PRODUCT_REFERENCE","References",["Product","GameDev"],"REDRIFT / Berserk","Public product video retained as a portfolio reference; the product domain in the registry is unavailable.","Portfolio Operations / Product Delivery; not presented as personal speaking.",["International product portfolio","Cross-functional delivery"],"projects-media/game-simulator.webp","reference_only",True),
rec("F06","puzzle-royale","Puzzle Royale — product reference","GitBook / YouTube","","https://puzzle-royale.gitbook.io/whitepaper/","PRODUCT_REFERENCE","References",["Product","GameDev"],"REDRIFT / Puzzle Royale","Public product documentation; the registry also includes a product video.","Portfolio Operations / Product Delivery; not presented as personal speaking.",["Product roadmap","MVP","International launch","LiveOps"],"projects-media/game-simulator.webp"),
rec("F07","cards-of-ethernity-video","Cards of Ethernity — product video","YouTube","","https://www.youtube.com/watch?v=Anp67xWqb7g","PRODUCT_REFERENCE","References",["Product","GameDev"],"REDRIFT / Cards of Ethernity","Public product video. The coe.gg domain from the registry now resolves to an unrelated product and is not used.","Portfolio Operations / Product Delivery; not presented as personal speaking.",["International product launch","Cross-functional portfolio delivery"],"projects-media/game-simulator.webp","reference_only",True),

rec("G01","mobileup-testimonial","MobileUp testimonial","MobileUp","","https://mobileup.ru/","PERSONAL_MENTION","Personal Mentions",["Product"],"Mobile Product Development","Potential testimonial record without a stable exact source URL.","Unconfirmed",[],"projects-media/fintech-wallet-mobile.webp","needs_recheck",False,note="Homepage does not confirm the specific testimonial attribution."),

rec("H01","chatex-cryptobank-introduction","Introduction to Chatex Cryptobank","Chatex on Medium","2021-07-29","https://chatexen.medium.com/introduction-to-chatex-cryptobank-the-simplest-finances-in-your-smartphone-58236c3eac5","PRODUCT_REFERENCE","References",["FinTech","Product","Growth"],"International FinTech Project","Official product publication describing the mobile-first financial platform and product modules.","Head of Product Projects; this is a product reference, not a formal employment or authorship claim.",["30K → 300K registered users","1K → 10K MAU","10× MAU growth","4× organic traffic growth"],"projects-media/chatex-cryptobank.webp"),
rec("H02","chatex-gtm-strategy","Chatex Go-to-Market strategy","Chatex on Medium","","https://chatexen.medium.com/how-are-we-gonna-scale-the-chatex-go-to-market-strategy-explained-4d4ae218e6d2","PRODUCT_REFERENCE","References",["FinTech","Growth","Marketing"],"International FinTech Project","Official product publication on Go-to-Market strategy.","Head of Product Projects; no authorship or formal employment claim.",[],"projects-media/chatex-cryptobank.webp","needs_recheck",False,note="Medium blocks automated access; exact page requires a manual recheck."),
rec("H03","chatex-founders-story","Chatex founder's story","Chatex on Medium","","https://chatexen.medium.com/the-founders-story-d21a267f8d8b","PRODUCT_REFERENCE","References",["FinTech","Product"],"International FinTech Project","Official company background publication.","Product reference only; no founder or authorship claim.",[],"projects-media/chatex-cryptobank.webp","needs_recheck",False,note="Medium blocks automated access; exact page requires a manual recheck."),
rec("H04","chatex-ama-recap","DeFi Raccoons × Chatex AMA recap","Medium","","https://medium.com/defiraccoons/ama-recap-defi-raccoons-x-chatex-809932e9128d","PROJECT_IN_MEDIA","Projects in the Media",["FinTech","PR","Growth"],"International FinTech Project","Community publication about the product.","Product reference only; no speaker claim without identity confirmation.",[],"projects-media/chatex-cryptobank.webp","needs_recheck",False,note="Medium blocks automated access; exact participation attribution requires manual confirmation."),

rec("S01","simdaq-platform-video","SIMDAQ platform presentation","YouTube","","https://www.youtube.com/watch?v=GOIhaW3cBHs&list=PLIGFTTG0_MxZULLSz7krz0E_YbxHJ3Foy&index=6","PRODUCT_REFERENCE","References",["FinTech","Product"],"SIMDAQ","Public video demonstrating the SIMDAQ platform.","Product reference; Roman is not labelled as the presenter without separate verification.",["Trading simulator","Historical data","Product demonstration"],"projects-media/simdaq-simulation.webp","reference_only",True),
rec("S02","gamblica-video-1","Gamblica product video","YouTube","","https://www.youtube.com/watch?v=5upgMatoD04","PRODUCT_REFERENCE","References",["Product","Blockchain","GameDev"],"Digital Finance Project / Gamblica","Public product video from the registry.","Product reference; not labelled as personal speaking without identity verification.",["International product","Product demonstration"],"projects-media/game-simulator.webp","reference_only",True),
rec("S03","gamblica-video-2","Gamblica presentation video","YouTube","","https://www.youtube.com/watch?v=exDisGISmNI&list=PLIGFTTG0_MxZULLSz7krz0E_YbxHJ3Foy&index=4","PRODUCT_REFERENCE","References",["Product","Blockchain","GameDev"],"Digital Finance Project / Gamblica","Public project presentation from the registry.","Product reference; not labelled as personal speaking without identity verification.",["Product presentation","International launch context"],"projects-media/game-simulator.webp","reference_only",True),
]

FILTERS = ["All", "By Me", "Speaking", "Projects in the Media", "Personal Mentions", "References"]
TOPICS = ["AI", "Project Management", "Product", "FinTech", "GameDev", "Blockchain", "Real Estate", "Digital Transformation", "Marketing", "PR", "Growth"]


def e(value): return html.escape(str(value), quote=True)


METRIKA = '''<!-- Yandex.Metrika counter -->
<script>(function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};m[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){if(document.scripts[j].src===r){return}}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})(window,document,'script','https://mc.yandex.ru/metrika/tag.js?id=111617582','ym');ym(111617582,'init',{ssr:true,webvisor:true,clickmap:true,ecommerce:'dataLayer',referrer:document.referrer,url:location.href,accurateTrackBounce:true,trackLinks:true});</script>
<noscript><div><img src="https://mc.yandex.ru/watch/111617582" style="position:absolute;left:-9999px" alt=""></div></noscript><!-- /Yandex.Metrika counter -->'''


def nav(prefix="../", current=""):
    cur = ' aria-current="page"' if current == "media" else ""
    return f'''<header class="media-head"><div class="media-shell media-head-inner"><a class="media-brand" href="{prefix}index.html">PERSONAL WEBSITE</a><nav aria-label="Main navigation"><a href="{prefix}index.html#overview">Overview</a><a href="{prefix}projects.html">Projects</a><a href="{prefix}experience.html">Experience</a><a{cur} href="{prefix}media/">Media</a><a href="{prefix}index.html#about">About</a><a href="{prefix}index.html#stack">Stack</a><a href="{prefix}index.html#contact">Contact</a><a class="media-cv" href="{prefix}Roman_Mironichev_One_Page_CV.pdf">CV ↓</a></nav></div></header>'''


def footer(prefix="../"):
    return f'''<footer class="media-footer"><nav aria-label="Footer navigation"><a href="{prefix}index.html#overview">Overview</a><a href="{prefix}projects.html">Projects</a><a href="{prefix}experience.html">Experience</a><a href="{prefix}media/">Media</a><a href="{prefix}index.html#about">About</a><a href="{prefix}index.html#stack">Stack</a><a href="{prefix}index.html#contact">Contact</a><a href="{prefix}Roman_Mironichev_One_Page_CV.pdf">CV ↓</a></nav></footer>'''


def card(r, prefix="../"):
    tags = " ".join(f"<span>{e(t)}</span>" for t in r["topics"][:3])
    language = '<span class="language-badge">RU · На русском</span>' if r["language"] == "ru" else '<span class="language-badge">EN</span>'
    type_label = "By Roman Mironichev" if r["kind"] == "BY_ME" else "Personal Mention" if r["kind"] == "PERSONAL_MENTION" else r["group"]
    type_class = "by-roman" if r["kind"] == "BY_ME" else "personal-mention" if r["kind"] == "PERSONAL_MENTION" else "reference"
    return f'''<article class="media-card {type_class}" data-group="{e(r['group'])}" data-topics="{e('|'.join(r['topics']))}"><a class="media-card-main" href="{e(r['slug'])}/"><div class="media-card-image"><img src="{prefix}{e(r['image'])}" alt="Preview from {e(r['source'])}: {e(r['title'])}" loading="lazy"></div><div class="media-card-body"><div class="media-source">Media: {e(r['source'])}</div><div class="media-meta"><span>No. {e(r['publication_number'])}</span><span>{e(r['display_date'])}</span>{language}</div><span class="media-type {type_class}">{e(type_label)}</span><h3>{e(r['title'])}</h3><p>{e(r['about'])}</p><p class="media-role">Role: {e(r['role'])}</p><div class="media-tags">{tags}</div></div></a><div class="media-card-actions"><a href="{e(r['slug'])}/">Details →</a><a href="{e(r['url'])}" target="_blank" rel="noopener noreferrer">Original ↗</a></div></article>'''


def editorial_section(r):
    item_id = r["id"]
    if item_id.startswith("E"): return "Raschetnye Resheniya"
    if item_id.startswith("D"): return "Samolet"
    if item_id == "P08": return "Emotional Intelligence"
    if item_id.startswith("B") or item_id == "S01": return "SIMDAQ"
    if item_id.startswith("C") or item_id.startswith("H"): return "International Startups"
    if item_id.startswith("F") or item_id in {"S02", "S03"}: return "Games & Digital Products"
    return "Articles & Other Media"


def editorial_groups(records):
    groups = []
    for record in records:
        label = editorial_section(record)
        if not groups or groups[-1][0] != label:
            groups.append((label, []))
        groups[-1][1].append(record)
    return "".join(
        f'<section class="media-editorial-group" data-editorial-group="{e(label)}"><h3 class="media-group-title">{e(label)}</h3><div class="media-grid all-grid">{"".join(card(record) for record in items)}</div></section>'
        for label, items in groups
    )


def page_head(title, description, canonical, css, og_image):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{e(canonical)}"><meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{e(canonical)}"><meta property="og:image" content="{e(BASE + '/' + og_image)}"><meta name="twitter:card" content="summary_large_image"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="{css}"></head>'''


def build():
    if not IN_REPOSITORY and OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "media").mkdir(parents=True, exist_ok=True)
    (OUT / "data").mkdir(parents=True, exist_ok=True)
    (OUT / "scripts").mkdir(parents=True, exist_ok=True)
    source_map_path = OUT / "data" / "media-image-sources.json"
    if not source_map_path.exists() and not IN_REPOSITORY:
        source_map_path = Path("work/media_image_sources.json")
    source_images = json.loads(source_map_path.read_text(encoding="utf-8")) if source_map_path.exists() else {}
    russian = {"A01", "A02", "A03", "A04", "P02", "P08", "P09", "D01", "D03", "D04", "D05", "E01", "E02", "E04"}
    verified_dates = {"E01": "2020-10-19", "E02": "2021-04-19", "F01": "2022-11-11"}
    for r in R:
        r["language"] = "ru" if r["id"] in russian else "en"
        if r["id"] in verified_dates:
            r["date"] = verified_dates[r["id"]]
        r["display_date"] = f"Published {r['date']}" if r["date"] else "Accessed 2026-08-16"
        r["image_source"] = source_images.get(r["id"], r["url"])
        local_image = OUT / "media-images" / f"{r['id'].lower()}.webp"
        r["image_origin"] = "project"
        if local_image.exists():
            r["image"] = f"media-images/{r['id'].lower()}.webp"
            r["image_origin"] = "original"
        simdaq_portfolio_images = {
            "B01": "projects-media/simdaq-dashboard.webp",
            "B02": "projects-media/simdaq-simulation.webp",
            "B03": "projects-media/simdaq-statistics.webp",
            "B04": "projects-media/simdaq-dashboard.webp",
            "B05": "projects-media/simdaq-simulation.webp",
            "B06": "projects-media/simdaq-statistics.webp",
            "B07": "projects-media/simdaq-dashboard.webp",
            "S01": "projects-media/simdaq-simulation.webp",
        }
        if r["id"] in simdaq_portfolio_images:
            r["image"] = simdaq_portfolio_images[r["id"]]
            r["image_origin"] = "project"
        if r["id"] in {"C06", "H01", "S02", "S03"}:
            r["published"] = False
            r["status"] = "needs_recheck"
            r["note"] = "Original publication preview could not be confirmed; withheld until the source is revalidated."
    public = [r for r in R if r["published"]]
    def editorial_order(r):
        item_id = r["id"]
        if item_id.startswith("E"): return (0, item_id)  # Raschetnye Resheniya
        if item_id.startswith("D"): return (1, item_id)  # Samolet
        if item_id == "P08": return (2, item_id)          # Emotional intelligence
        if item_id.startswith("B") or item_id == "S01": return (3, item_id)  # SIMDAQ
        if item_id.startswith("C") or item_id.startswith("H"): return (4, item_id)  # Startups
        if item_id.startswith("F") or item_id in {"S02", "S03"}: return (5, item_id)  # Games
        return (6, item_id)
    public.sort(key=editorial_order)
    for number, r in enumerate(public, 1):
        r["publication_number"] = f"{number:02d}"
    payload = {"generated": "2026-08-16", "filters": FILTERS, "topics": TOPICS, "records": R}
    (OUT / "data" / "media.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    featured = [r for r in public if r["featured"]][:8]
    index = page_head("Media & Publications — Roman Mironichev","Verified publications, authored articles, project coverage and product references across Product, FinTech, Digital Transformation and Growth.",f"{BASE}/media/","media.css",featured[0]["image"])
    index += f'''<body>{nav('../', 'media')}<main><section class="media-hero"><div class="media-shell"><p class="eyebrow">Editorial archive / Verified sources</p><h1>Media &amp;<br>Publications</h1><div class="media-hero-copy"><p>Selected articles, interviews, talks, and independent media coverage related to my work in product development, project management, technology, marketing, and digital transformation.</p><p>The collection includes my own publications as well as external coverage of products and companies I helped build, launch, manage, transform, or bring to market.</p><p>Where a publication covers a company or product rather than me personally, I indicate my role and the period of involvement separately.</p></div><div class="media-stats"><span><strong>{len(public)}</strong> confirmed materials</span><span><strong>{len(featured)}</strong> featured selections</span><span><strong>{len(R)-len(public)}</strong> held for recheck</span></div><a class="all-media-cta" href="#all-media">View all {len(public)} materials ↓</a></div></section><section class="media-section featured"><div class="media-shell"><div class="section-head"><div><p class="eyebrow">Selected evidence / 8 of {len(public)}</p><h2>Featured Media</h2></div><p>This is the featured selection. The complete catalogue with all {len(public)} confirmed links follows below.</p></div><div class="media-grid featured-grid">{''.join(card(r) for r in featured)}</div></div></section><section class="media-section all-media" id="all-media"><div class="media-shell"><div class="section-head"><div><p class="eyebrow">Complete source registry</p><h2>All Media — {len(public)}</h2></div><p>All confirmed materials are listed here. Filter by attribution first, then narrow by topic.</p></div><div class="filter-block"><div class="filter-row" aria-label="Filter by media type">{''.join(f'<button class="filter-button{" is-active" if x=="All" else ""}" type="button" data-filter-group="{e(x)}">{e(x)}</button>' for x in FILTERS)}</div><div class="filter-row topics" aria-label="Filter by topic"><button class="topic-button is-active" type="button" data-filter-topic="All">All topics</button>{''.join(f'<button class="topic-button" type="button" data-filter-topic="{e(x)}">{e(x)}</button>' for x in TOPICS)}</div></div><p class="results-count" aria-live="polite"></p><div class="editorial-groups">{editorial_groups(public)}</div><div class="empty-state" hidden>No confirmed materials match both filters.</div></div></section></main>{footer()}{METRIKA}<script src="media.js" defer></script></body></html>'''
    (OUT / "media" / "index.html").write_text(index, encoding="utf-8")

    for r in public:
        d = OUT / "media" / r["slug"]
        d.mkdir(exist_ok=True)
        related = [x for x in public if x["slug"] != r["slug"] and x["project"] == r["project"]][:3]
        facts = "".join(f"<li>{e(x)}</li>" for x in r["facts"])
        related_html = "".join(f'<a href="../{e(x["slug"])}/"><span>{e(x["source"])}</span>{e(x["title"])}</a>' for x in related)
        desc = f"{r['title']} — {r['source']}. Verified media record in Roman Mironichev's Product & Marketing Operations portfolio."
        page = page_head(f"{r['title']} — Media — Roman Mironichev",desc,f"{BASE}/media/{r['slug']}/","../media.css",r["image"])
        language = "RU · На русском" if r["language"] == "ru" else "EN"
        image_credit = f'Preview image from the <a href="{e(r["image_source"])}" target="_blank" rel="noopener noreferrer">original source</a>.' if r["image_origin"] == "original" else "No stable source preview was available; an owned project image is used."
        page += f'''<body>{nav('../../', 'media')}<main><article class="detail"><div class="media-shell"><a class="back-link" href="../">← All Media</a><div class="detail-grid"><div class="detail-main"><p class="eyebrow">{e(r['kind'].replace('_',' '))} / {e(r['source'])}</p><h1>{e(r['title'])}</h1><div class="detail-meta"><span>Publication No. {e(r['publication_number'])}</span><span>{e(r['display_date'])}</span><span>{e(r['project'])}</span><span>{e(language)}</span><span>{e(r['status'])}</span></div><img class="detail-hero" src="../../{e(r['image'])}" alt="Preview from {e(r['source'])}: {e(r['title'])}"><p class="image-credit">{image_credit}</p><section><h2>About the publication</h2><p>{e(r['about'])}</p></section><section><h2>About the project</h2><p>{e(r['project'])} — this page documents a public source connected to the product or company. It does not expand the source into unsupported personal claims.</p></section><section><h2>My role</h2><p>{e(r['role'])}</p></section>{f'<section><h2>Key facts</h2><ul>{facts}</ul></section>' if facts else ''}<a class="source-cta" href="{e(r['url'])}" target="_blank" rel="noopener noreferrer">Open original source ↗</a></div><aside><div class="attribution"><span>Attribution</span><strong>{e(r['kind'].replace('_',' '))}</strong><p>{'Written by Roman Mironichev.' if r['kind']=='BY_ME' else 'External or project-owned source. No personal authorship is claimed.'}</p></div>{f'<div class="related"><h2>Related media</h2>{related_html}</div>' if related else ''}</aside></div></div></article></main>{footer('../../')}{METRIKA}</body></html>'''
        (d / "index.html").write_text(page, encoding="utf-8")

    if not IN_REPOSITORY:
        shutil.copy2(Path("work/media.css"), OUT / "media" / "media.css")
        shutil.copy2(Path("work/media.js"), OUT / "media" / "media.js")
        (OUT / "scripts" / "build_media.py").write_text(HERE.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"records={len(R)} published={len(public)} withheld={len(R)-len(public)} detail_pages={len(public)}")


if __name__ == "__main__": build()
