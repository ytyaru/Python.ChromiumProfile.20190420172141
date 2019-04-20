#!/bin/bash
set -Ceu
#-----------------------------------------------------------------------------
# ブラウザのユーザ選択起動
# Created: 2019-04-20T07:43:01+0900
# Reference: http://chrome.half-moon.org/43.html
#-----------------------------------------------------------------------------
Chromium() { echo '/usr/bin/chromium-browser'; }
ProfileCmd() { echo "python3 ${HOME}/root/sys/workflow/script/py/tool/chromium/profile/ChromiumProfileCommand.py"; }
Run() {
	local -r usernames="$($(ProfileCmd) list -u | sort)"
	local -r selected="$(zenity --list --title="ブラウザ起動" --text="ユーザを選択してください" --height=300 --column="Users" ${usernames})"
	[ -z "$selected" ] && return
	local -r selectedDir="$($(ProfileCmd) get -d "$selected")"
	"$(Chromium)" --profile-directory="${selectedDir}"
}
Run

