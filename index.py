from decimal import Decimal

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def calculate_contrast_ratio(color1, color2):
    def relative_luminance(color):
        color = Decimal(color) / 255
        return color / Decimal('12.92') if color <= Decimal('0.03928') else ((color + Decimal('0.055')) / Decimal('1.055')) ** Decimal('2.4')

    r1, g1, b1 = color1
    r2, g2, b2 = color2

    l1 = relative_luminance(r1) * Decimal('0.2126') + relative_luminance(g1) * Decimal('0.7152') + relative_luminance(b1) * Decimal('0.0722')
    l2 = relative_luminance(r2) * Decimal('0.2126') + relative_luminance(g2) * Decimal('0.7152') + relative_luminance(b2) * Decimal('0.0722')

    if l1 > l2:
        brighter = l1
        darker = l2
    else:
        brighter = l2
        darker = l1

    contrast_ratio = (brighter + Decimal('0.05')) / (darker + Decimal('0.05'))
    return contrast_ratio

def calculate_value(contrast_ratio):
    value = ((float(contrast_ratio) - 1) / 20) * 1000
    return round(value)

def check_contrast(hex_color):
    color1 = hex_to_rgb(hex_color)
    color2 = hex_to_rgb("#000000")  # Black color
    contrast_ratio = calculate_contrast_ratio(color1, color2)
    value = calculate_value(contrast_ratio)
    
    return contrast_ratio, value

hex_color = input("Enter the HEX color value: ")
contrast_ratio, value = check_contrast(hex_color)
print(f"Contrast ratio against black (#000000): {contrast_ratio:.2f}")
print(f"Value calculated: {value}")
