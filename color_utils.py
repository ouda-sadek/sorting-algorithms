import colorsys
import matplotlib.pyplot as plt

class ColorUtils:
    # Helper class for working with colors
    
    def value_to_color(self, val, min_val, max_val):
        # Convert number to color using viridis colormap
        if max_val == min_val:
            return plt.cm.viridis(0.5)  # Middle color if all values equal
        normalized = (val - min_val) / (max_val - min_val)
        return plt.cm.viridis(normalized)
    
    def value_to_hue(self, val, min_val, max_val):
        # Convert number to HSV hue value
        if max_val == min_val:
            return 0.0  # Default hue if no range
        normalized = (val - min_val) / (max_val - min_val)
        r, g, b, _ = plt.cm.viridis(normalized)
        h, _, _ = colorsys.rgb_to_hsv(r, g, b)
        return h