(self["webpackChunk_jupyterlab_application_top"]=self["webpackChunk_jupyterlab_application_top"]||[]).push([[6504],{89129:(r,o,e)=>{"use strict";e.d(o,{Z:()=>A});var t=e(94015);var i=e.n(t);var n=e(23645);var c=e.n(n);var l=c()(i());l.push([r.id,".cm-s-liquibyte.CodeMirror {\n\tbackground-color: #000;\n\tcolor: #fff;\n\tline-height: 1.2em;\n\tfont-size: 1em;\n}\n.cm-s-liquibyte .CodeMirror-focused .cm-matchhighlight {\n\ttext-decoration: underline;\n\ttext-decoration-color: #0f0;\n\ttext-decoration-style: wavy;\n}\n.cm-s-liquibyte .cm-trailingspace {\n\ttext-decoration: line-through;\n\ttext-decoration-color: #f00;\n\ttext-decoration-style: dotted;\n}\n.cm-s-liquibyte .cm-tab {\n\ttext-decoration: line-through;\n\ttext-decoration-color: #404040;\n\ttext-decoration-style: dotted;\n}\n.cm-s-liquibyte .CodeMirror-gutters { background-color: #262626; border-right: 1px solid #505050; padding-right: 0.8em; }\n.cm-s-liquibyte .CodeMirror-gutter-elt div { font-size: 1.2em; }\n.cm-s-liquibyte .CodeMirror-guttermarker {  }\n.cm-s-liquibyte .CodeMirror-guttermarker-subtle {  }\n.cm-s-liquibyte .CodeMirror-linenumber { color: #606060; padding-left: 0; }\n.cm-s-liquibyte .CodeMirror-cursor { border-left: 1px solid #eee; }\n\n.cm-s-liquibyte span.cm-comment     { color: #008000; }\n.cm-s-liquibyte span.cm-def         { color: #ffaf40; font-weight: bold; }\n.cm-s-liquibyte span.cm-keyword     { color: #c080ff; font-weight: bold; }\n.cm-s-liquibyte span.cm-builtin     { color: #ffaf40; font-weight: bold; }\n.cm-s-liquibyte span.cm-variable    { color: #5967ff; font-weight: bold; }\n.cm-s-liquibyte span.cm-string      { color: #ff8000; }\n.cm-s-liquibyte span.cm-number      { color: #0f0; font-weight: bold; }\n.cm-s-liquibyte span.cm-atom        { color: #bf3030; font-weight: bold; }\n\n.cm-s-liquibyte span.cm-variable-2  { color: #007f7f; font-weight: bold; }\n.cm-s-liquibyte span.cm-variable-3, .cm-s-liquibyte span.cm-type { color: #c080ff; font-weight: bold; }\n.cm-s-liquibyte span.cm-property    { color: #999; font-weight: bold; }\n.cm-s-liquibyte span.cm-operator    { color: #fff; }\n\n.cm-s-liquibyte span.cm-meta        { color: #0f0; }\n.cm-s-liquibyte span.cm-qualifier   { color: #fff700; font-weight: bold; }\n.cm-s-liquibyte span.cm-bracket     { color: #cc7; }\n.cm-s-liquibyte span.cm-tag         { color: #ff0; font-weight: bold; }\n.cm-s-liquibyte span.cm-attribute   { color: #c080ff; font-weight: bold; }\n.cm-s-liquibyte span.cm-error       { color: #f00; }\n\n.cm-s-liquibyte div.CodeMirror-selected { background-color: rgba(255, 0, 0, 0.25); }\n\n.cm-s-liquibyte span.cm-compilation { background-color: rgba(255, 255, 255, 0.12); }\n\n.cm-s-liquibyte .CodeMirror-activeline-background { background-color: rgba(0, 255, 0, 0.15); }\n\n/* Default styles for common addons */\n.cm-s-liquibyte .CodeMirror span.CodeMirror-matchingbracket { color: #0f0; font-weight: bold; }\n.cm-s-liquibyte .CodeMirror span.CodeMirror-nonmatchingbracket { color: #f00; font-weight: bold; }\n.CodeMirror-matchingtag { background-color: rgba(150, 255, 0, .3); }\n/* Scrollbars */\n/* Simple */\n.cm-s-liquibyte div.CodeMirror-simplescroll-horizontal div:hover, .cm-s-liquibyte div.CodeMirror-simplescroll-vertical div:hover {\n\tbackground-color: rgba(80, 80, 80, .7);\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-horizontal div, .cm-s-liquibyte div.CodeMirror-simplescroll-vertical div {\n\tbackground-color: rgba(80, 80, 80, .3);\n\tborder: 1px solid #404040;\n\tborder-radius: 5px;\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-vertical div {\n\tborder-top: 1px solid #404040;\n\tborder-bottom: 1px solid #404040;\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-horizontal div {\n\tborder-left: 1px solid #404040;\n\tborder-right: 1px solid #404040;\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-vertical {\n\tbackground-color: #262626;\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-horizontal {\n\tbackground-color: #262626;\n\tborder-top: 1px solid #404040;\n}\n/* Overlay */\n.cm-s-liquibyte div.CodeMirror-overlayscroll-horizontal div, div.CodeMirror-overlayscroll-vertical div {\n\tbackground-color: #404040;\n\tborder-radius: 5px;\n}\n.cm-s-liquibyte div.CodeMirror-overlayscroll-vertical div {\n\tborder: 1px solid #404040;\n}\n.cm-s-liquibyte div.CodeMirror-overlayscroll-horizontal div {\n\tborder: 1px solid #404040;\n}\n","",{version:3,sources:["webpack://./node_modules/codemirror/theme/liquibyte.css"],names:[],mappings:"AAAA;CACC,sBAAsB;CACtB,WAAW;CACX,kBAAkB;CAClB,cAAc;AACf;AACA;CACC,0BAA0B;CAC1B,2BAA2B;CAC3B,2BAA2B;AAC5B;AACA;CACC,6BAA6B;CAC7B,2BAA2B;CAC3B,6BAA6B;AAC9B;AACA;CACC,6BAA6B;CAC7B,8BAA8B;CAC9B,6BAA6B;AAC9B;AACA,sCAAsC,yBAAyB,EAAE,+BAA+B,EAAE,oBAAoB,EAAE;AACxH,6CAA6C,gBAAgB,EAAE;AAC/D,4CAA4C;AAC5C,mDAAmD;AACnD,yCAAyC,cAAc,EAAE,eAAe,EAAE;AAC1E,qCAAqC,2BAA2B,EAAE;;AAElE,sCAAsC,cAAc,EAAE;AACtD,sCAAsC,cAAc,EAAE,iBAAiB,EAAE;AACzE,sCAAsC,cAAc,EAAE,iBAAiB,EAAE;AACzE,sCAAsC,cAAc,EAAE,iBAAiB,EAAE;AACzE,sCAAsC,cAAc,EAAE,iBAAiB,EAAE;AACzE,sCAAsC,cAAc,EAAE;AACtD,sCAAsC,WAAW,EAAE,iBAAiB,EAAE;AACtE,sCAAsC,cAAc,EAAE,iBAAiB,EAAE;;AAEzE,sCAAsC,cAAc,EAAE,iBAAiB,EAAE;AACzE,mEAAmE,cAAc,EAAE,iBAAiB,EAAE;AACtG,sCAAsC,WAAW,EAAE,iBAAiB,EAAE;AACtE,sCAAsC,WAAW,EAAE;;AAEnD,sCAAsC,WAAW,EAAE;AACnD,sCAAsC,cAAc,EAAE,iBAAiB,EAAE;AACzE,sCAAsC,WAAW,EAAE;AACnD,sCAAsC,WAAW,EAAE,iBAAiB,EAAE;AACtE,sCAAsC,cAAc,EAAE,iBAAiB,EAAE;AACzE,sCAAsC,WAAW,EAAE;;AAEnD,0CAA0C,uCAAuC,EAAE;;AAEnF,sCAAsC,2CAA2C,EAAE;;AAEnF,oDAAoD,uCAAuC,EAAE;;AAE7F,qCAAqC;AACrC,8DAA8D,WAAW,EAAE,iBAAiB,EAAE;AAC9F,iEAAiE,WAAW,EAAE,iBAAiB,EAAE;AACjG,0BAA0B,uCAAuC,EAAE;AACnE,eAAe;AACf,WAAW;AACX;CACC,sCAAsC;AACvC;AACA;CACC,sCAAsC;CACtC,yBAAyB;CACzB,kBAAkB;AACnB;AACA;CACC,6BAA6B;CAC7B,gCAAgC;AACjC;AACA;CACC,8BAA8B;CAC9B,+BAA+B;AAChC;AACA;CACC,yBAAyB;AAC1B;AACA;CACC,yBAAyB;CACzB,6BAA6B;AAC9B;AACA,YAAY;AACZ;CACC,yBAAyB;CACzB,kBAAkB;AACnB;AACA;CACC,yBAAyB;AAC1B;AACA;CACC,yBAAyB;AAC1B",sourcesContent:[".cm-s-liquibyte.CodeMirror {\n\tbackground-color: #000;\n\tcolor: #fff;\n\tline-height: 1.2em;\n\tfont-size: 1em;\n}\n.cm-s-liquibyte .CodeMirror-focused .cm-matchhighlight {\n\ttext-decoration: underline;\n\ttext-decoration-color: #0f0;\n\ttext-decoration-style: wavy;\n}\n.cm-s-liquibyte .cm-trailingspace {\n\ttext-decoration: line-through;\n\ttext-decoration-color: #f00;\n\ttext-decoration-style: dotted;\n}\n.cm-s-liquibyte .cm-tab {\n\ttext-decoration: line-through;\n\ttext-decoration-color: #404040;\n\ttext-decoration-style: dotted;\n}\n.cm-s-liquibyte .CodeMirror-gutters { background-color: #262626; border-right: 1px solid #505050; padding-right: 0.8em; }\n.cm-s-liquibyte .CodeMirror-gutter-elt div { font-size: 1.2em; }\n.cm-s-liquibyte .CodeMirror-guttermarker {  }\n.cm-s-liquibyte .CodeMirror-guttermarker-subtle {  }\n.cm-s-liquibyte .CodeMirror-linenumber { color: #606060; padding-left: 0; }\n.cm-s-liquibyte .CodeMirror-cursor { border-left: 1px solid #eee; }\n\n.cm-s-liquibyte span.cm-comment     { color: #008000; }\n.cm-s-liquibyte span.cm-def         { color: #ffaf40; font-weight: bold; }\n.cm-s-liquibyte span.cm-keyword     { color: #c080ff; font-weight: bold; }\n.cm-s-liquibyte span.cm-builtin     { color: #ffaf40; font-weight: bold; }\n.cm-s-liquibyte span.cm-variable    { color: #5967ff; font-weight: bold; }\n.cm-s-liquibyte span.cm-string      { color: #ff8000; }\n.cm-s-liquibyte span.cm-number      { color: #0f0; font-weight: bold; }\n.cm-s-liquibyte span.cm-atom        { color: #bf3030; font-weight: bold; }\n\n.cm-s-liquibyte span.cm-variable-2  { color: #007f7f; font-weight: bold; }\n.cm-s-liquibyte span.cm-variable-3, .cm-s-liquibyte span.cm-type { color: #c080ff; font-weight: bold; }\n.cm-s-liquibyte span.cm-property    { color: #999; font-weight: bold; }\n.cm-s-liquibyte span.cm-operator    { color: #fff; }\n\n.cm-s-liquibyte span.cm-meta        { color: #0f0; }\n.cm-s-liquibyte span.cm-qualifier   { color: #fff700; font-weight: bold; }\n.cm-s-liquibyte span.cm-bracket     { color: #cc7; }\n.cm-s-liquibyte span.cm-tag         { color: #ff0; font-weight: bold; }\n.cm-s-liquibyte span.cm-attribute   { color: #c080ff; font-weight: bold; }\n.cm-s-liquibyte span.cm-error       { color: #f00; }\n\n.cm-s-liquibyte div.CodeMirror-selected { background-color: rgba(255, 0, 0, 0.25); }\n\n.cm-s-liquibyte span.cm-compilation { background-color: rgba(255, 255, 255, 0.12); }\n\n.cm-s-liquibyte .CodeMirror-activeline-background { background-color: rgba(0, 255, 0, 0.15); }\n\n/* Default styles for common addons */\n.cm-s-liquibyte .CodeMirror span.CodeMirror-matchingbracket { color: #0f0; font-weight: bold; }\n.cm-s-liquibyte .CodeMirror span.CodeMirror-nonmatchingbracket { color: #f00; font-weight: bold; }\n.CodeMirror-matchingtag { background-color: rgba(150, 255, 0, .3); }\n/* Scrollbars */\n/* Simple */\n.cm-s-liquibyte div.CodeMirror-simplescroll-horizontal div:hover, .cm-s-liquibyte div.CodeMirror-simplescroll-vertical div:hover {\n\tbackground-color: rgba(80, 80, 80, .7);\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-horizontal div, .cm-s-liquibyte div.CodeMirror-simplescroll-vertical div {\n\tbackground-color: rgba(80, 80, 80, .3);\n\tborder: 1px solid #404040;\n\tborder-radius: 5px;\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-vertical div {\n\tborder-top: 1px solid #404040;\n\tborder-bottom: 1px solid #404040;\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-horizontal div {\n\tborder-left: 1px solid #404040;\n\tborder-right: 1px solid #404040;\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-vertical {\n\tbackground-color: #262626;\n}\n.cm-s-liquibyte div.CodeMirror-simplescroll-horizontal {\n\tbackground-color: #262626;\n\tborder-top: 1px solid #404040;\n}\n/* Overlay */\n.cm-s-liquibyte div.CodeMirror-overlayscroll-horizontal div, div.CodeMirror-overlayscroll-vertical div {\n\tbackground-color: #404040;\n\tborder-radius: 5px;\n}\n.cm-s-liquibyte div.CodeMirror-overlayscroll-vertical div {\n\tborder: 1px solid #404040;\n}\n.cm-s-liquibyte div.CodeMirror-overlayscroll-horizontal div {\n\tborder: 1px solid #404040;\n}\n"],sourceRoot:""}]);const A=l},23645:r=>{"use strict";r.exports=function(r){var o=[];o.toString=function o(){return this.map((function(o){var e=r(o);if(o[2]){return"@media ".concat(o[2]," {").concat(e,"}")}return e})).join("")};o.i=function(r,e,t){if(typeof r==="string"){r=[[null,r,""]]}var i={};if(t){for(var n=0;n<this.length;n++){var c=this[n][0];if(c!=null){i[c]=true}}}for(var l=0;l<r.length;l++){var A=[].concat(r[l]);if(t&&i[A[0]]){continue}if(e){if(!A[2]){A[2]=e}else{A[2]="".concat(e," and ").concat(A[2])}}o.push(A)}};return o}},94015:r=>{"use strict";function o(r,o){return c(r)||n(r,o)||t(r,o)||e()}function e(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function t(r,o){if(!r)return;if(typeof r==="string")return i(r,o);var e=Object.prototype.toString.call(r).slice(8,-1);if(e==="Object"&&r.constructor)e=r.constructor.name;if(e==="Map"||e==="Set")return Array.from(r);if(e==="Arguments"||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e))return i(r,o)}function i(r,o){if(o==null||o>r.length)o=r.length;for(var e=0,t=new Array(o);e<o;e++){t[e]=r[e]}return t}function n(r,o){var e=r&&(typeof Symbol!=="undefined"&&r[Symbol.iterator]||r["@@iterator"]);if(e==null)return;var t=[];var i=true;var n=false;var c,l;try{for(e=e.call(r);!(i=(c=e.next()).done);i=true){t.push(c.value);if(o&&t.length===o)break}}catch(A){n=true;l=A}finally{try{if(!i&&e["return"]!=null)e["return"]()}finally{if(n)throw l}}return t}function c(r){if(Array.isArray(r))return r}r.exports=function r(e){var t=o(e,4),i=t[1],n=t[3];if(typeof btoa==="function"){var c=btoa(unescape(encodeURIComponent(JSON.stringify(n))));var l="sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(c);var A="/*# ".concat(l," */");var a=n.sources.map((function(r){return"/*# sourceURL=".concat(n.sourceRoot||"").concat(r," */")}));return[i].concat(a).concat([A]).join("\n")}return[i].join("\n")}},26504:(r,o,e)=>{"use strict";e.r(o);e.d(o,{default:()=>A});var t=e(93379);var i=e.n(t);var n=e(89129);var c={};c.insert="head";c.singleton=false;var l=i()(n.Z,c);const A=n.Z.locals||{}},93379:(r,o,e)=>{"use strict";var t=function r(){var o;return function r(){if(typeof o==="undefined"){o=Boolean(window&&document&&document.all&&!window.atob)}return o}}();var i=function r(){var o={};return function r(e){if(typeof o[e]==="undefined"){var t=document.querySelector(e);if(window.HTMLIFrameElement&&t instanceof window.HTMLIFrameElement){try{t=t.contentDocument.head}catch(i){t=null}}o[e]=t}return o[e]}}();var n=[];function c(r){var o=-1;for(var e=0;e<n.length;e++){if(n[e].identifier===r){o=e;break}}return o}function l(r,o){var e={};var t=[];for(var i=0;i<r.length;i++){var l=r[i];var A=o.base?l[0]+o.base:l[0];var a=e[A]||0;var s="".concat(A," ").concat(a);e[A]=a+1;var d=c(s);var u={css:l[1],media:l[2],sourceMap:l[3]};if(d!==-1){n[d].references++;n[d].updater(u)}else{n.push({identifier:s,updater:f(u,o),references:1})}t.push(s)}return t}function A(r){var o=document.createElement("style");var t=r.attributes||{};if(typeof t.nonce==="undefined"){var n=true?e.nc:0;if(n){t.nonce=n}}Object.keys(t).forEach((function(r){o.setAttribute(r,t[r])}));if(typeof r.insert==="function"){r.insert(o)}else{var c=i(r.insert||"head");if(!c){throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.")}c.appendChild(o)}return o}function a(r){if(r.parentNode===null){return false}r.parentNode.removeChild(r)}var s=function r(){var o=[];return function r(e,t){o[e]=t;return o.filter(Boolean).join("\n")}}();function d(r,o,e,t){var i=e?"":t.media?"@media ".concat(t.media," {").concat(t.css,"}"):t.css;if(r.styleSheet){r.styleSheet.cssText=s(o,i)}else{var n=document.createTextNode(i);var c=r.childNodes;if(c[o]){r.removeChild(c[o])}if(c.length){r.insertBefore(n,c[o])}else{r.appendChild(n)}}}function u(r,o,e){var t=e.css;var i=e.media;var n=e.sourceMap;if(i){r.setAttribute("media",i)}else{r.removeAttribute("media")}if(n&&typeof btoa!=="undefined"){t+="\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(n))))," */")}if(r.styleSheet){r.styleSheet.cssText=t}else{while(r.firstChild){r.removeChild(r.firstChild)}r.appendChild(document.createTextNode(t))}}var C=null;var b=0;function f(r,o){var e;var t;var i;if(o.singleton){var n=b++;e=C||(C=A(o));t=d.bind(null,e,n,false);i=d.bind(null,e,n,true)}else{e=A(o);t=u.bind(null,e,o);i=function r(){a(e)}}t(r);return function o(e){if(e){if(e.css===r.css&&e.media===r.media&&e.sourceMap===r.sourceMap){return}t(r=e)}else{i()}}}r.exports=function(r,o){o=o||{};if(!o.singleton&&typeof o.singleton!=="boolean"){o.singleton=t()}r=r||[];var e=l(r,o);return function r(t){t=t||[];if(Object.prototype.toString.call(t)!=="[object Array]"){return}for(var i=0;i<e.length;i++){var A=e[i];var a=c(A);n[a].references--}var s=l(t,o);for(var d=0;d<e.length;d++){var u=e[d];var C=c(u);if(n[C].references===0){n[C].updater();n.splice(C,1)}}e=s}}}}]);
//# sourceMappingURL=6504.f578fea4ca18a937babd.js.map?v=f578fea4ca18a937babd