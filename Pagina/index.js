/* ---------- MODULES ---------- */
const bodyParser = require('body-parser');
const chalk = require('chalk');
const compression = require('compression');
const cors = require('cors');
const express = require('express');
const flash = require('connect-flash');
const helmet = require('helmet');
const methodOverride = require('method-override');
const morgan = require('morgan');
const path = require('path');
const session = require('express-session');

/* ---------- CLASSES & INSTANCES ---------- */
const app = express();

/* ---------- CONSTANTS ---------- */
const PORT = 8080;

/* ----- Express ----- */
app.set('view engine', 'ejs');
app.use('/', express.static(path.join(__dirname, 'public'))); // URL path begins at /public.

if (process.env.NODE_ENV === 'production') {
    app.set('trust proxy', 1);
}

// Middleware
app.use(bodyParser.urlencoded({ extended: false })); // Parse application/x-www-form-urlencoded.
app.use(bodyParser.json()); // Parse application/json.
app.use(cors());
app.use(compression()); // Compress all responses.
app.use(
    helmet({
        contentSecurityPolicy: false,
    })
);
app.use(flash());
app.use(methodOverride('_method', { methods: ['POST', 'GET'] })); // Process POST request suffixed with ?_method=DELETE or ?_method=PUT.
app.use(morgan('dev'));
app.use(session({
    name: 'qid',
    secret: process.env.SESSION_SECRET || 'dQw4w9WgXcQ', // run `node -e "console.log(crypto.randomBytes(32).toString('hex'))"` in console to generate secret.
    resave: false,
    saveUninitialized: false,
    cookie: {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        maxAge: 1000 * 60 * 60 * 24 * 2 * 365 // 2 years
    }
}));


/* ---------- ROUTES ---------- */
app.use('/', require('./routes/index'));


/* ---------- LAUNCH ---------- */
app.listen(PORT, () => {
    console.log(chalk.blue(`Server running at http://localhost:${PORT}/`));
});