const express = require('express');
const app = express();
const mysql = require('mysql2/promise');

const pool = mysql.createPool({
  host: 'localhost',
  user: 'example_user',
  password: 'example_user_password',
  database: 'example_db'
});

app.get('/scores', async (req, res) => {
  console.log('GET /scores1');
  const { address, walletType, page = 1, limit = 10 } = req.query;

  if (!address || !walletType) {
    return res.status(400).send('Bad Request: Address and walletType are required parameters');
  }

  const offset = (page - 1) * limit;

  try {
    const conn = await pool.getConnection();
    const [rows, fields] = await conn.query('SELECT * FROM reputation_score WHERE address = ? AND wallet_type = ? LIMIT ? OFFSET ?', [address, walletType, limit, offset]);
    conn.release();
    res.setHeader('Content-Type', 'application/json');
    res.send({ data: rows, page, limit });
  } catch (err) {
    console.error(err);
    res.status(500).send('Internal Server Error');
  }
});


const server = app.listen(3000, () => {
  console.log('Server listening on port 3000');
});

module.exports = { app, pool, server };