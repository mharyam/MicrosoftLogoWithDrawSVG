import drawSvg as draw

d = draw.Drawing(1080, 720, origin='center', displayInline=False)

# Draw a rectangle
r = draw.Rectangle(-10, 0, 50, 50, fill='#F25022')
d.append(r)

g = draw.Rectangle(50, 0, 50, 50, fill='#7FBA00')
d.append(g)

b = draw.Rectangle(-10, -60, 50, 50, fill='#00A4EF')
d.append(b)

y = draw.Rectangle(50, -60, 50, 50, fill='#FFB900')
d.append(y)

d.append(draw.Text('Microsoft', 100, 120, -40, fill='#737373'))  # Text with font size 8

# Display
d.saveSvg("microsoft.svg")
print("HERE o000000000000000000000")

