const express = require('express');
const app = express();
const marp = require('@marp-team/marp-cli/marp-core');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.post('/convert', (req, res) => {
  const { article } = req.body;
  const { html, css } = marp.render(article, {
    html: true,
    engine: 'github', // Choose your preferred Marp engine (github or powerpoint)
  });

  res.send({ html, css });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
