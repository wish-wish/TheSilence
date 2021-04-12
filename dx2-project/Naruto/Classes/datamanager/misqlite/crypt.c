#include "crypt.h"
#include "malloc.h"
#include "aes.h"

#define KEY_LENGHT 256
#define BLOCK_SIZE 16

static aes_context _Gctx;

int aes_encrypt(unsigned char* pData, unsigned int data_len,
	unsigned char* key, unsigned int len_of_key)
{
	int i, count, offset;
	unsigned char* sour = (unsigned char*)malloc(data_len);
	memcpy(sour, pData, data_len);

	count = data_len / BLOCK_SIZE;
	aes_setkey_enc(&_Gctx, key, KEY_LENGHT);
	for(i = 0; i < count; i++)
	{
		offset = i * BLOCK_SIZE;
		aes_crypt_ecb(&_Gctx, AES_ENCRYPT, (const unsigned char*)sour + offset, pData + offset);
	}
	free(sour);
	return 0;
}

int aes_decrypt(unsigned char* pData, unsigned int data_len,
	unsigned char* key, unsigned int len_of_key)
{
	int i, count, offset;
	unsigned char* sour = (unsigned char*)malloc(data_len);
	memcpy(sour, pData, data_len);
	
	count = data_len / BLOCK_SIZE;
	aes_setkey_dec(&_Gctx, key, KEY_LENGHT);
	for(i = 0; i < count; i++)
	{
		offset = i * BLOCK_SIZE;
		aes_crypt_ecb(&_Gctx, AES_DECRYPT, (const unsigned char*)sour + offset, pData + offset);
	}
	free(sour);
	return 0;
}