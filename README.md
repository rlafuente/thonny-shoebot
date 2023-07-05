# thonny-shoebot

*A Shoebot plug-in for Thonny*

Use the [Thonny Python IDE](https://thonny.org/) as an editor for [Shoebot](https://shoebot.net) scripts. *Thonny-shoebot* is a plug-in that configures Thonny for use with Shoebot, a Python (3.8+) framework for creative coding vector graphics and animations using a set of simple Python commands.


## Instructions

If you already have some version of Thonny *that includes Python 3.8+* on your computer, you can skip straight to step 4.

1. Download and install the Thonny IDE from [https://github.com/thonny/thonny/releases](https://github.com/thonny/thonny/releases). Expanding the *Assets* will reveal the downloads for Windows/macOS/Linux --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/01-download-thonny.png)
   
   For your convenience, here are direct links to the downloads for Thonny 4.0.0b3:
   
    - [thonny-4.0.0b3.exe](https://github.com/thonny/thonny/releases/download/v4.0.0b3/thonny-4.0.0b3.exe) 🢠 for Windows
    - [thonny-4.0.0b3.pkg](https://github.com/thonny/thonny/releases/download/v4.0.0b3/thonny-4.0.0b3.pkg) 🢠 for MacOS
    - [thonny-4.0.0b3-x86_64.tar.gz](https://github.com/thonny/thonny/releases/download/v4.0.0b3/thonny-4.0.0b3-x86_64.tar.gz) 🢠 for Linux
   
   The thonny-shoebot plug-in will run fine with Thonny 4 (currently in beta) because it ships with Python 3.10. If you want to use a Thonny 3 release, use the [Thonny 3.3.7](https://github.com/thonny/thonny/releases/tag/v3.3.7) *-alt* version for your platform. The alt-variants are bundled with Python 3.9.5 (instead of 3.7.9).

   

2. Start Thonny. If you're running it for the first time, just accept the *Standard* settings.

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/02-start-splash.png)

3. Once Thonny is open, select *Tools > Manage plugins...*

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.01-manage-plug-ins.png)

   Then search for and install the __thonny-shoebot__ plug-in --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.02-install-plug-in.png)

   You must __restart Thonny__ after this step.

4. When you've restarted Thonny, select *py5 > Imported mode for py5* --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.01-activate-imported-mode.png)

   Click *Proceed* to download, extract, and set up JDK-17 (if you need to know: the plug-in installs JDK in the Thonny user-config directory). Thonny only needs to download JDK the first time you switch to imported mode.

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.02-download-jdk.png)

   You'll be notified once this process completes --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.03-download-jdk-done.png)

5. *This step is optional.* There are several Thonny settings that I recommend you apply for working with py5 (including a Processing 4 inspired theme, Kyanite). You can apply those settings in one simple step using  *py5 > Apply recommended py5 settings*

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05-apply-recommended-settings.png)

6. When the py5 *Imported mode for py5* option is checked, Thonny can run your py5 code --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.01-imported-activated.png)

   Test out an [imported mode](https://py5.ixora.io/content/py5_modes.html#imported-mode) sketch by clicking the green play button (or using the F5 or Ctrl+R keyboard shortcuts). Here is some code:

   ```python
   def setup():
       size(300, 200)
       rect_mode(CENTER)

   def draw():
       rect(mouse_x, mouse_y, 10, 10)
   ```

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.02-running-sketch.png)

   NOTE: This mode also runs [static mode](https://py5.ixora.io/content/py5_modes.html#static-mode) sketches (when you don't need a `draw()` function for animation).

   Click the stop-sign (🛑) button in the Thonny toolbar to stop your sketch.


## Useful py5 resources

py5 is a new version of Processing for Python 3.8+. It makes the Java Processing jars available to the CPython interpreter using JPype. It can do just about everything Processing can do, except with Python instead of Java code. Here are some useful py5 resources (alphabetically listed) --

* [py5 cheatsheet](https://raw.githubusercontent.com/tabreturn/processing.py-cheat-sheet/master/py5/py5_cc.pdf)
* [py5 discussions/forum](https://github.com/py5coding/py5generator/discussions)
* [py5 documentation](http://py5.ixora.io/)
* [py5 examples](https://github.com/py5coding/py5examples)
* [Processing forum (Python channel)](https://discourse.processing.org/c/processing-py/9)
* [Villares' sketch-a-day archive](https://abav.lugaralgum.com/sketch-a-day/)


## Credits

Thanks [villares](https://github.com/villares/thonny-py5-runner) for inspiring me to develop this plug-in, [hx2A](https://github.com/hx2A/) for the awesome [py5 project](https://py5.ixora.io/), and the [Thonny folks](https://github.com/thonny) for their fantastic IDE. The *Color selector* incorporates Juliette Monsel's excellent [tkColorPicker](https://github.com/j4321/tkColorPicker) module.


## Todo List

See [discussions on GitHub repo](https://github.com/tabreturn/thonny-py5mode/discussions/17). This plug-in is a work in progress ... please report issues [here](https://github.com/tabreturn/thonny-py5mode/issues).
