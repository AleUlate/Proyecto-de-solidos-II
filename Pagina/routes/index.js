/* ---------- MODULES ---------- */
const express = require('express');

/* ---------- CLASSES & INSTANCES ---------- */
const router = express.Router();

/* ---------- ROUTES ---------- */

router.get('/', (_req, res) => {
    res.render('landing');
});

router.get('/calculator', (_req, res) => {
    res.render('calculator');
});

module.exports = router;