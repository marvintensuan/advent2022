# Advent of Code 2022

These are my Advent of Code 2022 solutions.

Compared to previous year, I think I have gotten better at *Typing* especially at Generics. Thanks mostly to Python 3.10 and 3.11's effort to make type hints more expresive. My code style have also been influenced by my exposure to *functional programming* and *array programming* paradigms.

## Thoughts
### Day 2, 4 and 5

As someone who is self-studying programming paradigms and type theory, I was quick to appreciate Python's type hints. Given my lack of experience, I may have also fallen into its pitfalls, if there are any. Nevertheless, one thing I've definitely observed is that this time, running `mypy` has resulted in me opening the debugger less (one time to be exact).

**Day 2** - if one tried to look at my commit history, Day 2 originally looked totally different. It was imperative. One function had weird guard clause. I was asking the wrong questions. One thing I know I wanted though is that I did not want to copy other's solution where they have a dictionary of a dictionary of possible combinations. As a business user by day, I get that; dictionaries *map* one value to another. However, it felt anti-DRY. Soon as I realized that this can be solved by indexing, everything started to click, by [this commit](https://github.com/marvintensuan/advent2022/commit/7e82), Day 2 effectively has no dictionaries left.👏👏👏

Earlier this year, I wrote [a blog post about indexing](https://dev.to/marvintensuan/quick-peek-under-the-hood-indexing-and-slicing-in-python-3a5i) and slicing in Python.

**Day 4**  - I don't use `set` every day and much less so for `frozenset`s. Glad I was able to spot the need as it arise. Also, `all` and `any` are both here. The snippet got removed but I think it's mentioning that the principle of *Easier to Ask Permission than Forgiveness* (EAFP) vs *Look Before You Leap* (LBYL) are among my This Year I Learned's.

**Day 5** - this is noticeably the first one which did not have a separate solution. My main solution function *inverted control* 😉 to other function. And then seeing as those functions can also operate at the same exact way, I combined them into one and then added modality.

### Day 3 and 6

Another thing I learned this year is Python's `more_itertools` library. I really had a field day with iterables this year, here's another [one](https://gist.github.com/marvintensuan/7e99873e71528947f6d6c9d7dd5c456c) from my GitHub gists.

### Day 7

**Day 7** may be solved with or without trees. But this year I learned about (intro to) graph theory, so let's do it this way. I used the `networkx` libary for building the graph. Is it worth it? Part 2 was quick to solve so there's that.

My Part 2 solution also has an `assert` statement. I remember a discussion early this year about whether or not there should be `assert`s in production code.

These lines:

```python
    to_delete = space_required - (total_space - space_used_current)
    assert total_space == space_used_current + (space_required - to_delete)
```

Most people would prefer to put `total_space - space_used_current` in it's own separate variable. I would argue that *Naming is hard* and *Readability counts*.

Another unpopular naming choice I made is that most solutions assigned uppercase to things like `TOTAL_SPACE`, as per PEP 8. I made it a *kwarg*, which doesn't necessitate for that. 


## Here's to 2023

...