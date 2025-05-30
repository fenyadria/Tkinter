def garis_pinggir_teks(canvas, x, y, text, font, fill, outline_color="White", outline_width=2):
    offsets = [
        (-outline_width, -outline_width),
        (-outline_width, 0),
        (-outline_width, outline_width),
        (0, -outline_width),
        (0, outline_width),
        (outline_width, -outline_width),
        (outline_width, 0),
        (outline_width, outline_width),
    ]
    outline_ids = []
    for ox, oy in offsets:
        outline_id = canvas.create_text(x + ox, y + oy, text=text, font=font, fill=outline_color, anchor="center")
        outline_ids.append(outline_id)

    main_id = canvas.create_text(x, y, text=text, font=font, fill=fill, anchor="center")

    return outline_ids, main_id
