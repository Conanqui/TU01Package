#include "gdef.h"
#include "swrite.h"
#include "bbattery.h"
#include "unif01.h"
#include "ufile.h"

int main (int argc, char *argv[])
{
    swrite_Basic = FALSE;
    unif01_Gen *gen1;
	gen1 = ufile_CreateReadText (argv[1], 1);
    bbattery_BlockAlphabit(gen1, 1048576, 0, 32);
    ufile_DeleteReadText(gen1);
}