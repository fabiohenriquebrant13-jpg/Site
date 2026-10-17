// Gera variantes WebP sem substituir as imagens originais.
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

process.chdir(path.resolve(__dirname, '..'));
fs.mkdirSync('assets/responsive', { recursive: true });

(async () => {
  const jobs = [
    ['assets/logo-160.webp', [80]],
    ['assets/nova/motor-hero-clean.webp', [480, 800, 960]],
    ...['motores-eletricos', 'motobomba', 'redutores', 'capacitores', 'rolamentos', 'pecas-componentes']
      .map(name => [`assets/nova/${name}.webp`, [480, 800]]),
    ...['IMG-20261003-WA0022', 'IMG-20261003-WA0021', 'IMG-20261003-WA0009',
      'IMG-20261003-WA0025', 'IMG-20261003-WA0005', 'IMG-20261003-WA0026-nova']
      .map(name => [`assets/${name}.webp`, [640, 960]]),
    ...['rebobinamento', 'manutencao-preventiva']
      .map(name => [`assets/nova/${name}.webp`, [960]])
  ];
  const images = [];
  for (const [source, widths] of jobs) {
    for (const width of widths) {
      const output = `assets/responsive/${path.basename(source, '.webp')}-${width}.webp`;
      await sharp(source)
        .resize({ width, withoutEnlargement: true })
        .webp({ quality: source.includes('logo') ? 90 : 82, effort: 6 })
        .toFile(output);
      images.push({ source, output, width,
        originalBytes: fs.statSync(source).size, bytes: fs.statSync(output).size });
    }
  }
  console.log(JSON.stringify({ variants: images.length, images }, null, 2));
})().catch(error => {
  console.error(error);
  process.exit(1);
});
