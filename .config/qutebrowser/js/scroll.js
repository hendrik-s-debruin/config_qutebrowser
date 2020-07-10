quteBrowserShouldScroll = true;
function quteBrowserScrollPage() {
	window.scrollBy(0, 1);
	if(quteBrowserShouldScroll){
		scrolldelay = setTimeout('quteBrowserScrollPage()', 1 );
	}
}
quteBrowserScrollPage();
