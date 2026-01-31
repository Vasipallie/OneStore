import express from 'express';
import cookieParser from 'cookie-parser';
import { dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
import { createClient } from '@supabase/supabase-js';
import bodyParser from 'body-parser';
import path from 'path';

const app = express();
const PORT = process.env.PORT || 5000;
app.use(cookieParser());
const supabase = createClient("https://gkkpwnqytanjsdjojqur.supabase.co", "sb_publishable_Sdn9s5v2IvPSjYlbjDDp_g_YnXbK_N8");

// Middleware data stuff, important for onestore web to run
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'views')));
app.use(bodyParser.urlencoded({ extended: true }));

app.route('/').get((req, res) => {
    res.render('index', { title: "OneStore Web" });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
    console.log(`Visit http://localhost:${PORT}`);
});