# QKP instances

## URL

These instances are cited from

- \[group1 - 3\] [An iterated “hyperplane exploration” approach for the quadratic knapsack problem](https://www.sciencedirect.com/science/article/pii/S0305054816302015)
- \[QKPLIB\] https://data.mendeley.com/datasets/82pxy6yv49/1

## Format

- `n` is the number of the items
- `v_(i,i)` is the linear coefficients of the item `i`
- `v_(i,j)` os the quadratic coefficients between the item `i` and `j`
- `c` is the capacity of the knapsack
- `w_i` is the weights of the item `i`

```txt
n
v_(1,1), v_(2,2), ..., v_(n,n)
v_(2,3), v_(2,4), ..., v_(2, n)
...
v_(n-2,n-1), v_(n-2,n)
v_(n-1,n)

c
w_1, w_2, ..., w_n
```

The below is an example.
This is the same as `instances/sample.txt`.

```txt
10
91 78 22 4 48 85 46 81 3 26
55 23 35 44 5 91 95 26 40
92 11 20 43 71 83 27 65
7 57 33 38 57 63 82
100 87 91 83 44 48
69 57 79 89 21
9 40 22 26
50 6 7
71 52
17

145
34 33 12 3 43 26 10 2 48 39
```

Objective function:

$$
\begin{align}
    \mathrm{max}~~91x_1 &+ 78x_2 + 22x_3 + 4x_4 + 48x_5 + 85x_6 + 46x_7 + 81x_8 + 3x_9 + 26x_{10} \\
     & + 55x_1x_2 + 23x_1x_3 + 35x_1x_4 + 44x_1x_5 + 5x_1x_6 + 91x_1x_7 + 95x_1x_8 + 26x_1x_9 + 40 x_1x_{10} \notag \\
     & + 92x_2x_3 + 11x_2x_4 + 20x_2x_5 + 43x_2x_6 + 71x_2x_7 + 83x_2x_8 + 27x_2x_9 + 65x_2x_{10} \notag \\
     & + 7x_3x_4 + 57x_3x_5 + 33x_3x_6 + 38x_3x_7 + 57x_3x_8 + 63x_3x_9 + 82x_3x_{10} \notag \\
     & + 100x_4x_5 + 87x_4x_6 + 91x_4x_7 + 83x_4x_8 + 44x_4x_9 + 48x_4x_{10} \notag \\
     & + 69x_5x_6 + 57x_5x_7 + 79x_5x_8 + 89x_5x_9 + 21x_5x_{10} \notag \\
     & + 9x_6x_7 + 40x_6x_8 + 22x_6x_9 + 26x_6x_{10} \notag \\
     & + 50x_7x_8 + 6x_7x_9 + 7x_7x_{10} \notag \\
     & + 71x_8x_9 + 52x_8x_{10} \notag \\
     & + 17x_9x_{10} \notag \\
    \mathrm{s.t.}~~34x_1 & + 33x_2 + 12x_3 + 3x_4 + 43x_5 + 26x_6 + 10x_7 + 2x_8 + 48x_9 + 29x_{10}\leq 145\\
    x_i \in {0,1}, &\forall i \in \{1, \dots, n\}
\end{align}
$$

See in detail [here](https://cedric.cnam.fr/~soutif/QKP/).

## Note

In this repository instance-files, we OMIT

- reference of the instance like `r_10_100_13`,
- `0/1` constraint type because all instance has 0,
- some comments because all instance has NO cooment
- Densiry

## Other

If there is any issues, please publish Issue or Pull-Request.
