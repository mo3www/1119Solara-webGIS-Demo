import solara
import plotly.express as px

@solara.component
def Page():
    # 'with' 語法會自動將內部的所有元件放入 Column 容器
    with solara.Column(align="center"):
        solara.Markdown("## 馬太鞍溪簡介")
        solara.Markdown("---")
        solara.Markdown("馬太鞍溪發源自丹大山北邊，是花蓮溪的支流之一。關門古道越過東段最高點的倫太文山之後，先沿稜下降到倫太文西鞍，之後便往下繞過兩個大山溝，再沿西北向稜線下降到海拔1800公尺處的馬太鞍溪上游，下溪處為一寬闊平坦地，為清軍駐紮之營盤，有七株超過15公尺高的紅檜，故稱為「巨木營盤址」，古道過溪之後，便一路陡上至中央山脈主稜。此處的溪水清澈見底，水深及膝，溪中處處是白色大石，加上兩岸林木蓊鬱，十分清幽。")
        solara.Image(image="/file/GM_027.jpg", width="50%")

