export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  var d = req.body;
  var collectibles = Array.isArray(d.collectibles) ? d.collectibles.join(', ') : d.collectibles || '—';

  var text = `🎮 *Nouvelle demande MyWedGame*\n\n`
    + `👤 Marié : ${d.groom}\n`
    + `👰 Mariée : ${d.bride}\n`
    + `📅 Date : ${d.date}\n`
    + `📍 Lieu : ${d.location}\n`
    + `🎯 Niveaux : ${d.levels}\n`
    + `💎 Collectibles : ${collectibles}\n`
    + `📧 Email : ${d.email}\n\n`
    + `📖 *Histoire :*\n${d.story || '—'}\n\n`
    + `🎲 *Détails fun :*\n${d.details || '—'}`;

  var resp = await fetch(`https://api.telegram.org/bot${process.env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: process.env.TELEGRAM_CHAT_ID,
      text: text,
      parse_mode: 'Markdown'
    })
  });

  if (!resp.ok) return res.status(500).json({ error: 'Telegram send failed' });
  return res.status(200).json({ ok: true });
}
