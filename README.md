# Date-Driven Destiny & Lifecycle Generator

A client-side JavaScript engine that processes an explicit date of birth string to output structured personal profiles, zodiac sign parsing, relationship tendencies, and lifecycle projections.

## Running the Project

1. Clone or download this project's code directory to your desktop environment.
2. Open `index.html` inside any browser instance to test calculations.

## Code Design & Architecture

Unlike typical generators that rely on pure math randomizers, this implementation uses a deterministic approach:
* **Zodiac Engine:** Evaluates calendar boundary rules via a map structure of start/end arrays to dynamically capture the true astrological sign.
* **Deterministic Seeding:** Sums day, month, and year values to create a unique integer seed. This seed runs against modulo operations to ensure the same date of birth persistently renders identical text matrices and lifespans.
* **Semantic Structure:** Leverages native HTML5 date input validation rules directly, bypassing heavy manual fallback code overhead.

