#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <dmarc.h>

#define HUMAN_ERR_SIZ 128
#define BUFFER_SIZ 512

int
main(int argc, char *argv[]) {
	char buf[BUFFER_SIZ],err[HUMAN_ERR_SIZ];
	char *in;
	int in_len;
	u_char **out,**f_out;

	/* Read Input */
	in_len = BUFFER_SIZ+1;
	in = calloc(1,in_len);
	while(fgets(buf,BUFFER_SIZ,stdin) != NULL) {
		if(strlen(in) + strlen(buf) >= in_len) {
			in_len *= 2;
			in = realloc(in,in_len);
		}
		strncat(in,buf,in_len);
	}

	/* Parse */
	out = opendmarc_xml(in,in_len,err,HUMAN_ERR_SIZ);
	f_out = out;

	/* Print Human Readable Version */
	while(*out != NULL) {
		printf("%s\n",*out);
		out++;
	}

	/* Cleanup */
	opendmarc_util_clearargv(f_out);
	return EXIT_SUCCESS;
}
