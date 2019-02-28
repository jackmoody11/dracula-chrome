import json

# To make image from command line with imagemagick:
# convert -size 100x100 xc:#990000 whatever.png

#################### Colors ####################
background = [40, 42, 54]
background_translucent = [40, 42, 54, 0.6]
current_line = [68, 71, 90]
selection = [68, 71, 90]
foreground = [248, 248, 242]
comment = [98, 114, 164]
cyan = [139, 233, 253]
green = [80, 250, 123]
orange = [255, 184, 108]
pink = [255, 121, 198]
purple = [189, 147, 249]
red = [255, 85, 85]
yellow = [241, 250, 140]

#################### Tints ####################
background_tint = [231, 14.9, 18.4]
background_tint_light = [231, 14.9, 28]

manifest = {
    "description": "Chrome Theme based on Dracula",
    "manifest_version": 2,
    "name": "Dracula",
    "theme": {
        "colors": {
            # Color of the bookmark element’s text
            "bookmark_text": foreground,
            # Background color of all the toolbar buttons
            "button_background": red,
            # Color of the window control buttons (close, maximize, etc.)
            "control_background": background,
            # The color of the frame, that covers the smaller outer frame
            "frame": background,
            # The color of the frame, that covers the smaller outer frame when inactive
            "frame_inactive": background_translucent,
            # The color of the frame, that covers the smaller outer frame when incognito
            "frame_incognito": background,
            # The color of the frame, that covers the smaller outer frame when incognito and inactive
            "frame_incognito_inactive": background_translucent,
            # Theme's inner background color
            "ntp_background": background,
            "ntp_header": red,
            "ntp_link": cyan,
            "ntp_link_underline": cyan,
            "ntp_section": background,
            "ntp_section_link": cyan,
            # Color of underline of links in the section area
            "ntp_section_link_underline": cyan,
            # Color of text in the section
            "ntp_section_text": foreground,
            # Color of all the text that comes in the inner background area
            "ntp_text": foreground,
            # Color of text, in the title of background tabs
            "tab_background_text": foreground,
            # Color of text, in the title of current tab
            "tab_text": foreground,
            # Color of the toolbar background
            "toolbar": current_line
        },
        "images": {
            "theme_button_background": "images/theme_button_background.png",
            # Area that is behind the tabs
            "theme_frame": "images/theme_frame.png",
            # Theme frame when inactive
            "theme_frame_inactive": "images/theme_frame.png", 
            # Theme frame when incognito
            "theme_frame_incognito": "images/theme_frame_incognito.png",
            # Theme frame when incognito and inactive
            "theme_frame_incognito_inactive": "images/theme_frame_incognito_inactive.png",
            # Image that appears at the top left of the frame
            # "theme_frame_overlay": "",
            # Image that appears at the top left of the frame when inactive
            # "theme_frame_overlay_inactive": "",
            # Image that will be displayed in the 'theme created by' section
            # "theme_ntp_attribution": "",
            # Theme's inner background - the large white space is covered by this.
            "theme_ntp_background": "images/theme_ntp_background.png",
            # Area that covers tabs which are not active
            "theme_tab_background": "images/theme_tab_background.png",
        },
        "properties": {
            "ntp_background_alignment": "",
            "ntp_background_repeat": "",
            "ntp_logo_alternate": "",
        },
        "tints": {
            "background_tab": background_tint,
            "frame": background_tint,
            "frame_inactive": background_tint,
            "frame_incognito": background_tint,
            "frame_incognito_inactive": background_tint
        }
    },
    "version": "1.0"
}

if __name__ == '__main__':
    manifest_json = json.dumps(manifest, indent=2, sort_keys=True)
    with open('manifest.json', 'w') as f:
        f.write(manifest_json)
