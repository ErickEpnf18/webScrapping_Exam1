# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 20:07:40 2021

@author: aguil
"""

import requests
from pymongo import MongoClient
page = requests.get("https://olympics.com/tokyo-2020/es/")
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')


page = requests.get("https://m.facebook.com/olympics/")
soup = BeautifulSoup(page.content, 'html.parser')
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

# <div class="scrollAreaBody accelerate" id="u_1c_2_2c" data-sigil="scroll-area-body" style="backface-visibility: hidden; transform: translate(0px, 0px);"><a class="_484w selected scrollAreaColumn" href="/olympics/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6n_dY" data-sigil="msite-pages-presence-current-tab"><span class="_6zf">Inicio</span></a><a class="_484w scrollAreaColumn" href="/olympics/about/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6o_vy"><span class="_6zf">Información</span></a><a class="_484w scrollAreaColumn" href="/olympics/photos/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6p_uc"><span class="_6zf">Fotos</span></a><a class="_484w scrollAreaColumn" href="/olympics/videos/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6q_wl"><span class="_6zf">Vídeos</span></a><a class="_484w scrollAreaColumn" href="/olympics/live_videos/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6r_JP"><span class="_6zf">En directo</span></a><a class="_484w scrollAreaColumn" href="/olympics/events/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6s_/9"><span class="_6zf">Eventos</span></a><a class="_484w scrollAreaColumn" href="/olympics/posts/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6t_k9"><span class="_6zf">Publicaciones</span></a><a class="_484w scrollAreaColumn" href="/olympics/groups/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6u_22"><span class="_6zf">Grupos</span></a><a class="_484w scrollAreaColumn" href="/olympics/community/?ref=page_internal&amp;mt_nav=0" style="min-width: 11%" id="u_1c_6v_i1"><span class="_6zf">Comunidad</span></a></div>
list_container = soup.find_all(class_="rootcontainer")


# list_section = list_container.find_all(class_="_484w scrollAreaColumn")
# list_items2 = list_section.find_all(class_="_484w scrollAreaColumn")



# period_tags = seven_day.select(".tombstone-container .period-name")
# periods = [pt.get_text() for pt in period_tags]#este es el pt en cada get_text() 

# dropdown = soup2.find_all(class_="dropdown-menu")
print(list_container)