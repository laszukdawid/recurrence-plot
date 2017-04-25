# recurrence-plot

# Shortly
Tools for creating recurrence plot.

# Instruction
See `plot_recurrance.py` for example on how to use it.
In short, import `rec_plot` function from `plot_recurrance.py` and with help of NumPy (`np`) and matplotlib (`plt`) write:
```python
    sig = np.random.uniform(size=100)
    rec = rec_plot(sig)
    plt.imshow(rec)
    plt.show()
```
Few inspirational plots below.

# Blog post with description:
Small blog post on using visualising Intrinsic Mode Frequency (IMFs), i.e. output of Empirical Mode Decomposition, can be found here:
https://laszukdawid.com/2015/09/04/emd-on-audio-wav-and-recurrance-plots/

# Cool-looking plots
[example]: examples/chainsaw/images/chainsaw_imfR_3.png "Reccurance plot of an IMF"

