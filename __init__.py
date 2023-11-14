from aqt import mw, dialogs
from aqt.utils import show_info, qconnect
from aqt.qt import *

def display_notes() -> None:
    """Display notes which are tagged "leech" but have no suspended cards"""

    found_note_ids : list = []

    search_string : str = "tag:leech"
    for note_id in mw.col.find_notes(search_string, False):
        suspended_cards_found : bool = False

        card_ids = mw.col.card_ids_of_note(note_id)
        for card_id in card_ids:
            card = mw.col.get_card(card_id)
            if card.queue == -1:
                suspended_cards_found = True
                break

        if not suspended_cards_found:
            found_note_ids.append(note_id)

    if len(found_note_ids) == 0:
        show_info(f"All notes tagged \"leech\" have at least one suspended card.")
    else:
        nid_string = ",".join([str(x) for x in found_note_ids])
        browser = dialogs.open('Browser', mw)
        # Don't need to include search_string here because the set of nids has already been filtered.
        # But include it as a visual cue to the user.
        browser.setFilter(f'{search_string} nid:{nid_string}')
        browser.setWindowState(
            browser.windowState() & ~Qt.WindowState.WindowMinimized | Qt.WindowState.WindowActive
        )

action = QAction("Notes tagged \"leech\" that have no suspended cards", mw)
qconnect(action.triggered, display_notes)
mw.form.menuTools.addAction(action)
