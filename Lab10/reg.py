import re

# txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR.-_*/+"
#
# print(re.findall("or", txt))
# print(re.findall(".", txt))
# print(re.findall( "or.", txt))
# print(re.findall("..\.", txt))
#
#
# print("Hello\nWorld")
#
# print(r"Hello\nWorld")
#
# print()
# print(re.findall(r"\w", txt))
# print(re.findall(r"\W", txt))
# print()
# print(re.findall(r"\d", txt))
# print(re.findall(r"\D", txt))
# print()
# print(re.findall(r"\s", txt))
# print(re.findall(r"\S", txt))
# print()
# print(re.findall(r"[bcdfghjklmnpqrstvxz]", txt))
# print()
#------------------------TASK 1 & 2
mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

# print(re.findall(r"(?:^|\s)([\w.]+@[\w.]+\.\w+)", mtxt))
print(re.findall(r"(?:^|\s)([\w.]+@[\w.]+\.\w+)", mtxt))
#------------------------END TASK 1 & 2


#------------------------TASK 3 MAIN

f = open("tabla.html", encoding="utf-8")
txt = f.read()

episodes = re.findall(r"<td class=\"svtTablaTime\">\s+"
                      r"(\d+\.\d+)\s+"
                      r"</td>\s+"
                      r"<td class=\"svtJsTablaShowInfo\">\s+"
                      r"<h4 class=\"svtLink-hover svtTablaHeading\">\s+"
                      r"Simpsons\s+"
                      r"</h4>\s+"
                      r"<div class=\"svtJsStopPropagation\">\s+"
                      r"<div class=\"svtTablaTitleInfo svtHide-Js\">\s+"
                      r"<div class=\"svtTablaContent-Description\">\s+"
                      r"<p class=\"svtXMargin-Bottom-10px\">\s+Amerikansk animerad komediserie från [\d-]+\. Säsong (\d+)\. Del (\d+) av (\d+)\.(.+?)\s+"
                      r"</p>", txt)
for record in episodes:
    tid = record[0]
    season = record[1]
    episode = record[2]+"\\"+record[3]
    description = record[4]
    print("-"*50)
    print("""
        Tid: {}
        Säsong: {}
        Avsnitt: {}
        Handling: {}
          """.format(tid, season, episode, description))
