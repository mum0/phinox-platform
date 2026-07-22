/**
 * Future production Tailwind build config — NOT yet consumed by any
 * template (Phase 1 templates still use the Stitch CDN <script> + inline
 * config per shell, to guarantee pixel fidelity with the source). This file
 * transcribes Family A (Checkout) as the default `theme.extend`; Family B's
 * divergent tokens are layered in once IMPLEMENTATION_PLAN.md open question
 * #5 (which family is canonical) is resolved.
 */
module.exports = {
  darkMode: "class",
  content: ["./templates/**/*.html", "./apps/**/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        "on-surface-variant": "#c4c7c7",
        "surface-variant": "#343535",
        "on-background": "#e3e2e2",
        "primary-container": "#0f0f0f",
        "surface-container-highest": "#343535",
        "tertiary-container": "#210700",
        "surface-container": "#1e2020",
        primary: "#c8c6c5",
        "surface-dim": "#121414",
        "surface-container-low": "#1a1c1c",
        "surface-container-lowest": "#0d0e0f",
        error: "#ffb4ab",
        "surface-container-high": "#292a2a",
        "error-container": "#93000a",
        "secondary-container": "#4a4949",
        "surface-bright": "#38393a",
        "on-primary": "#313030",
        surface: "#121414",
        "on-secondary": "#313030",
        outline: "#8e9192",
        secondary: "#c8c6c5",
        "outline-variant": "#444748",
        "on-surface": "#e3e2e2",
        tertiary: "#ffb596",
        "on-tertiary": "#581e00",
        background: "#121414",
        "fire-orange": "#E85D04",
      },
      borderRadius: { DEFAULT: "0px", lg: "0px", xl: "0px", full: "9999px" },
      spacing: {
        unit: "4px",
        "touch-target-min": "48px",
        gutter: "1px",
        "margin-desktop": "40px",
        "margin-mobile": "16px",
      },
      fontFamily: {
        "button-text": ["Archivo Narrow"],
        "body-base": ["JetBrains Mono"],
        "label-technical": ["JetBrains Mono"],
        "headline-md": ["Archivo Narrow"],
        "display-lg": ["Archivo Narrow"],
        "headline-md-mobile": ["Archivo Narrow"],
      },
    },
  },
  plugins: [require("@tailwindcss/forms"), require("@tailwindcss/container-queries")],
};
