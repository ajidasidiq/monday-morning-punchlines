# monday-morning-punchlines

[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/ajidasidiq/monday-morning-punchlines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/ajidasidiq/monday-morning-punchlines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

Entry for the [make.fun bounty "Monday Morning Punchlines"](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc): one joke about Monday mornings, 200 characters at most, judged on laughs.

## The entry

> I tried ghosting Monday morning. It texted back from my own number: 'see you at 9.'

83 characters. The joke turns on the reply: you can't ghost a day that already has your number — literally. No alarm clock, no coffee, no "I hate Mondays": just Monday texting back from your own phone.

## How it works

`main.py` writes that single line to `/output/entry.txt` and gate-checks it first: UTF-8 text, 1–200 characters, not only whitespace, a single line, and it verifies the bytes on disk match the entry exactly.

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
