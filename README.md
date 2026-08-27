# Tender Calculator — Telegram WebApp

A single `index.html` file. No backend, no build step, no dependencies.
Calculates tender lot profitability right inside Telegram.

## What it calculates
- Bid price after your price reduction (dumping)
- Purchase cost, logistics, other expenses, bank fees
- VAT 12%, including input VAT credit from the supplier
- Income tax: simplified 3% of turnover or general 20% of profit
- Net profit, margin, ROI, profit per unit
- **Break-even threshold** — the maximum price reduction and the minimum bid price
- Bid security deposit
- Bid structure as a stacked bar

## WebApp features
- Theme (light/dark) and accent colour taken from Telegram `themeParams`
- MainButton shows live net profit and sends the calculation to the chat (`sendData`)
- Haptic feedback on toggles and sliders
- Currency switch: KZT / KGS / RUB
- Works as a normal web page outside Telegram (the button copies the summary to the clipboard)

## Deploy (GitHub Pages, 2 minutes)
```bash
git init && git add . && git commit -m "tender calculator"
git branch -M main
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```
Settings → Pages → Source: `main` / root. URL: `https://<user>.github.io/<repo>/`
(Telegram requires **https** — GitHub Pages, Netlify, Vercel or Cloudflare Pages all work.)

## Connect it to a bot
1. @BotFather → `/newapp` or `/setmenubutton` → point it at the page URL.
2. Or run `bot.py`:
```bash
pip install aiogram
BOT_TOKEN=... WEBAPP_URL=https://<user>.github.io/<repo>/ python bot.py
```
`sendData` from the WebApp arrives in the `F.web_app_data` handler as ready-made text.

## Changing the rates
Rates live in one place — the `model()` function in `index.html`: `VAT = 12`,
`0.03` (simplified regime), `0.20` (general regime). One line each to retarget
another jurisdiction.
