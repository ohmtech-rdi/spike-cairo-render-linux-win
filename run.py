#!/usr/bin/env python3

import cairocffi



if __name__ == '__main__':
   pt_per_mm = 72 / 25.4
   width, height = 210 * pt_per_mm, 297 * pt_per_mm  # A4 portrait
   surface = cairocffi.PDFSurface ('cairo_render.pdf', width, height)
   context = cairocffi.Context (surface)
   context.select_font_face ('D-DIN Bold', cairocffi.FONT_SLANT_NORMAL, cairocffi.FONT_WEIGHT_NORMAL)
   context.set_font_size (12.0)
   context.move_to (200, 200)
   context.text_path ('SYNC')
   context.set_source_rgb (0, 0, 0)
   context.fill ()
