def calculate_color_contrast(contrast):
  """Calculates the color contrast value based on the contrast against black.

  Args:
    contrast: The contrast against black.

  Returns:
    The color contrast value.
  """

  value = ((contrast - 1) / 20) * 1000
  return round(value, 1)

def main():
  """The main function."""

  contrast = float(input("Insert the colour contrast against black: "))
  color_contrast_value = calculate_color_contrast(contrast)
  print("The color contrast value is:", color_contrast_value)

if __name__ == "__main__":
  main()
