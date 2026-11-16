"""Free printable PDFs: a shot log and a site rotation chart. Zones match the app's Simple body map (12 sites)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "printables")
LOGO = os.path.join(ROOT, "assets", "logo-96.png")
os.makedirs(OUT, exist_ok=True)

PURPLE, INK, MUTED, LINE, SOFT = HexColor("#6a3fd6"), HexColor("#1d1433"), HexColor("#5c5470"), HexColor("#cfc6e6"), HexColor("#ece5fb")
W, H = letter
M = 40
LINK = "www.nexdose.app/?utm_source=printable"

SITES = ["Right arm (side)", "Left arm (side)", "Right flank", "Left flank",
         "Right abdomen, upper", "Left abdomen, upper", "Right abdomen, lower", "Left abdomen, lower",
         "Right thigh, front", "Right thigh, side", "Left thigh, front", "Left thigh, side"]


def header(c, title, sub):
    c.drawImage(LOGO, M, H - M - 26, 26, 26, mask="auto")
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 20); c.drawString(M + 36, H - M - 20, title)
    c.setFillColor(MUTED); c.setFont("Helvetica", 10); c.drawString(M, H - M - 46, sub)


def footer(c, page=None):
    c.setStrokeColor(LINE); c.line(M, 50, W - M, 50)
    c.setFillColor(MUTED); c.setFont("Helvetica", 8.5)
    c.drawString(M, 36, "Free from Nexdose. For your own records only; not medical advice. Follow your healthcare provider's guidance.")
    c.setFillColor(PURPLE); c.setFont("Helvetica-Bold", 9)
    t = "Rather not use paper? The Nexdose app does this for you, free on iPhone: "
    c.drawString(M, 23, t)
    c.setFont("Helvetica", 9); x = M + c.stringWidth(t, "Helvetica-Bold", 9)
    c.drawString(x, 23, "www.nexdose.app")
    c.linkURL("https://" + LINK, (x, 20, x + c.stringWidth("www.nexdose.app", "Helvetica", 9), 32))
    if page:
        c.setFillColor(MUTED); c.setFont("Helvetica", 8.5); c.drawRightString(W - M, 36, page)


def shot_log():
    c = canvas.Canvas(os.path.join(OUT, "nexdose-shot-log.pdf"), pagesize=letter)
    c.setTitle("Nexdose Shot Log"); c.setAuthor("Nexdose")
    cols = [("Date", 62), ("Time", 46), ("Medicine", 104), ("Dose", 56), ("Site #", 40), ("Weight", 50), ("Notes", 0)]
    tw = W - 2 * M
    cols[-1] = ("Notes", tw - sum(w for _, w in cols[:-1]))
    rows = 26
    for p in (1, 2):
        header(c, "Shot Log", "Write down each shot as you take it. Use the site numbers from the Site Rotation Chart.")
        c.setFillColor(INK); c.setFont("Helvetica", 10)
        y0 = H - M - 72
        c.drawString(M, y0, "Name:"); c.setStrokeColor(LINE); c.line(M + 34, y0 - 2, M + 250, y0 - 2)
        c.drawString(M + 270, y0, "Year:"); c.line(M + 300, y0 - 2, M + 380, y0 - 2)
        top = y0 - 20; rh = (top - 70) / (rows + 1)
        c.setFillColor(PURPLE); c.roundRect(M, top - rh, tw, rh, 4, fill=1, stroke=0)
        x = M; c.setFillColor(white); c.setFont("Helvetica-Bold", 9.5)
        for n, w in cols:
            c.drawString(x + 6, top - rh + 7, n); x += w
        for r in range(rows):
            y = top - rh * (r + 2)
            if r % 2:
                c.setFillColor(SOFT); c.rect(M, y, tw, rh, fill=1, stroke=0)
            c.setFillColor(MUTED); c.setFont("Helvetica", 7)
            c.drawString(M + 3, y + rh - 8, str(r + 1 + (p - 1) * rows))
        c.setStrokeColor(LINE); c.setLineWidth(.6)
        for r in range(rows + 1):
            y = top - rh * (r + 1); c.line(M, y, M + tw, y)
        x = M
        for _, w in cols[:-1]:
            x += w; c.line(x, top - rh, x, top - rh * (rows + 1))
        c.rect(M, top - rh * (rows + 1), tw, rh * rows, fill=0, stroke=1)
        footer(c, f"Page {p} of 2")
        c.showPage()
    c.save()


def rounded(c, x, y, w, h, r, fill, stroke=None):
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke); c.setLineWidth(1.4)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)


def rotation_chart():
    c = canvas.Canvas(os.path.join(OUT, "nexdose-site-rotation-chart.pdf"), pagesize=letter)
    c.setTitle("Nexdose Site Rotation Chart"); c.setAuthor("Nexdose")
    header(c, "Site Rotation Chart", "The 12 sites from the Nexdose body map. Write the date each time you use a site, and spread your shots around.")
    # Body outline (front view), centred in the left half
    cx, base = 170, 300
    body, edge = HexColor("#f2eff8"), HexColor("#b9addb")
    c.setStrokeColor(edge); c.setLineWidth(1.2); c.setFillColor(body)
    c.circle(cx, base + 330, 28, fill=1, stroke=1)                    # head
    c.roundRect(cx - 10, base + 290, 20, 16, 4, fill=1, stroke=0)      # neck
    shapes = [(cx - 58, base - 70, 52, 210, 24), (cx + 6, base - 70, 52, 210, 24),   # legs
              (cx - 62, base + 90, 124, 70, 20), (cx - 62, base + 120, 124, 180, 26),  # hips, torso
              (cx - 98, base + 120, 26, 176, 13), (cx + 72, base + 120, 26, 176, 13)]  # arms
    for x, y, w, h, r in shapes:
        c.roundRect(x, y, w, h, r, fill=1, stroke=1)
    for x, y, w, h, r in shapes[:4]:
        c.roundRect(x + 1.2, y + 1.2, w - 2.4, h - 2.4, r - 1, fill=1, stroke=0)
    # Zones: (number, x, y, w, h) — numbering matches SITES
    zw = HexColor("#d9cdfb")
    zones = [(1, cx - 96, base + 180, 22, 100), (2, cx + 74, base + 180, 22, 100),
             (3, cx - 58, base + 186, 14, 34), (4, cx + 44, base + 186, 14, 34),
             (5, cx - 40, base + 206, 36, 30), (6, cx + 4, base + 206, 36, 30),
             (7, cx - 40, base + 170, 36, 30), (8, cx + 4, base + 170, 36, 30),
             (9, cx - 30, base - 10, 24, 110), (10, cx - 54, base - 10, 22, 110),
             (11, cx + 6, base - 10, 24, 110), (12, cx + 32, base - 10, 22, 110)]
    for n, x, y, w, h in zones:
        rounded(c, x, y, w, h, 6, zw, PURPLE)
        c.setFillColor(PURPLE); c.circle(x + w / 2, y + h / 2, 8, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 8.5); c.drawCentredString(x + w / 2, y + h / 2 - 3, str(n))
    c.setFillColor(MUTED); c.setFont("Helvetica-Oblique", 8.5)
    c.drawCentredString(cx, base - 92, "Front view. Your right is on the left of the picture.")
    # Site list with date boxes
    lx, ty = 330, H - M - 92
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 11); c.drawString(lx, ty, "Site")
    c.drawString(lx + 128, ty, "Dates used")
    rh = 37; boxes = 4; bw = (W - M - (lx + 128)) / boxes
    for i, name in enumerate(SITES):
        y = ty - 14 - rh * (i + 1)
        if i % 2 == 0:
            c.setFillColor(SOFT); c.rect(lx - 6, y, W - M - lx + 6, rh, fill=1, stroke=0)
        c.setFillColor(PURPLE); c.circle(lx + 8, y + rh / 2, 8, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 8.5); c.drawCentredString(lx + 8, y + rh / 2 - 3, str(i + 1))
        c.setFillColor(INK); c.setFont("Helvetica", 9.5)
        parts = name.split(", ")
        if len(parts) == 2:
            c.drawString(lx + 22, y + rh / 2 + 2, parts[0] + ","); c.drawString(lx + 22, y + rh / 2 - 10, parts[1])
        else:
            c.drawString(lx + 22, y + rh / 2 - 3, name)
        c.setStrokeColor(LINE); c.setLineWidth(.6)
        for b in range(boxes):
            bx = lx + 128 + b * bw
            c.rect(bx + 2, y + 6, bw - 4, rh - 12, fill=0, stroke=1)
    # Tips
    ty2 = 120
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 10.5); c.drawString(M, ty2, "How to use it")
    c.setFont("Helvetica", 9.5); c.setFillColor(MUTED)
    tips = ["Before each shot, look for the site with the oldest date, or one you haven't used yet.",
            "Write the date in that site's next empty box, and the site number in your Shot Log.",
            "Ask your provider which sites suit your medicine and how far apart to space your shots."]
    for k, t in enumerate(tips):
        c.drawString(M, ty2 - 16 - k * 14, f"{k + 1}.  {t}")
    footer(c)
    c.showPage(); c.save()


if __name__ == "__main__":
    shot_log(); rotation_chart()
