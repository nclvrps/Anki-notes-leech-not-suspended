Anki add-on for displaying notes which are tagged "leech" but have no suspended cards

== Description ==

Cards which are answered incorrectly too many times become leeches. When this happens, the note associated with the card receives a "leech" tag, and by default the card is suspended. (Note that Anki lets you configure the Leech Threshold and Leech Action in each deck's Options)

When manually unsuspending a card, it is easy to forget to remove the "leech" tag from the note. It is also cumbersome to check manually for the rare cases where a "leech"-tagged note actually has more than one suspended card.

This add-on finds notes which are tagged "leech" but have no suspended cards, and displays them in the Browse window. You can then choose to untag them or take any other action.

== How it could be done manually instead ==

Without this add-on, you could perform the same function manually by doing the following:

* Switch to Notes mode in the Browse window.
* Search for is:suspended
* Click on the first line of results, and then select all lines. (In Windows this can be done with Ctrl-A, or by scrolling down to the final line of results and holding Shift while clicking on it).
* Do "Add Tags..." and apply a tag like "is_suspended" or any other newly invented tag name of your choice.
* Search for tag:leech -tag:is_suspended to get the desired list.
* Clean up afterward by deleting the "is_suspended" tag.
